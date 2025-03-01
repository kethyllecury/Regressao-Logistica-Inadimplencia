import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

df = pd.read_excel("contas_receber.xlsx", parse_dates=["vencimento"]) #tornar datatime

df["hoje"] = pd.Timestamp.today()
df["dias_atraso"] = (df["hoje"] - df["vencimento"]).dt.days

# aqui vamos remover os dados duplicados pois há vários pedidos na mesma nota fiscal

df_agrupado = df.drop_duplicates(subset=["contato.id", "valor"]).copy()

# tornando dados de numeros para categoricos

mapeamento_situacao = {
    1: "Pago",
    2: "Em Aberto",
    3: "Atrasado",
    5: "Cancelado"
}

df_agrupado["situacao_atual"] = df_agrupado["situacao"].map(mapeamento_situacao)

df_agrupado.loc[:, "situacao_atual"] = df_agrupado["situacao"].map(mapeamento_situacao)
df_agrupado.loc[:, "inadimplente"] = (
    (df_agrupado["dias_atraso"] > 30) & 
    (~df_agrupado["situacao_atual"].isin(["Cancelado"]))
).astype(int)

# aqui criamos a estatísticas por cliente

clientes = df_agrupado.groupby("contato.id").agg(
    total_divida=("valor", "sum"),
    qtd_contas_vencidas=("inadimplente", "sum"),
    media_atraso=("dias_atraso", "mean")
).reset_index()

# variáveis de entrada (X) e saída (y)

X = clientes[["total_divida", "qtd_contas_vencidas", "media_atraso"]].fillna(0)
y = (clientes["qtd_contas_vencidas"] > 1).astype(int)  # cliente com mais de 1 conta vencida = inadimplente

# normalizar os dados

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# dividimos os dados em treino e teste (80% treino, 20% teste)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# treinando o modelo de Regressão Logística

model = LogisticRegression()
model.fit(X_train, y_train)

# fazendo as previsões

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]  # probabilidades de inadimplência

clientes_inadimplentes = df_agrupado[df_agrupado["inadimplente"] == 1]

plt.figure(figsize=(10, 6))

# Plotar a distribuição de inadimplentes vs não inadimplentes

plt.hist(df_agrupado["dias_atraso"][df_agrupado["inadimplente"] == 1], bins=20, alpha=0.7, label="Inadimplente", color='red')
plt.hist(df_agrupado["dias_atraso"][df_agrupado["inadimplente"] == 0], bins=20, alpha=0.7, label="Não Inadimplente", color='green')

# Adicionar título e rótulos

plt.title('Distribuição dos Dias de Atraso: Inadimplente vs Não Inadimplente')
plt.xlabel('Dias de Atraso')
plt.ylabel('Número de Clientes')
plt.legend()

# exibir gráfico

plt.show()

# gráfico de dispersao com os inadimplentes em diferentes dias 

plt.figure(figsize=(10, 6))

plt.scatter(clientes_inadimplentes["dias_atraso"], clientes_inadimplentes["inadimplente"], 
            c='red', alpha=0.7, label="Inadimplente")

plt.title('Gráfico de Dispersão: Dias de Atraso vs Inadimplência (Inadimplentes Apenas)')
plt.xlabel('Dias de Atraso')
plt.ylabel('Inadimplente (1: Sim)')

plt.legend()
plt.show()

# avaliar o modelo

print("Acurácia:", accuracy_score(y_test, y_pred))
print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred))
print("Relatório de Classificação:\n", classification_report(y_test, y_pred))
print("AUC-ROC:", roc_auc_score(y_test, y_prob))
print(clientes_inadimplentes.head(50))

