# Previsão de Inadimplência em Contas a Receber - Zero Furo

Este projeto utiliza **Regressão Logística** para prever a inadimplência de clientes com base em dados de contas a receber. A análise é feita para identificar clientes que têm maior probabilidade de não pagar suas dívidas, ajudando a empresa **Zero Furo** a tomar decisões informadas sobre ações de cobrança e gestão de crédito.

## Objetivo

O principal objetivo deste projeto é construir um modelo preditivo capaz de identificar quais clientes têm maior probabilidade de se tornarem inadimplentes, ou seja, com dívidas em aberto por mais de 30 dias. O modelo usa variáveis como o total da dívida, a quantidade de contas vencidas e a média de dias de atraso para realizar essa previsão.

## Estrutura do Projeto

Este repositório contém o código que realiza as seguintes tarefas:

1. **Leitura e Preparação dos Dados**:
   - O arquivo Excel `contas_receber.xlsx` contém os dados de contas a receber de clientes.
   - O código realiza o pré-processamento dos dados, incluindo a conversão de valores de datas e a remoção de duplicatas.

2. **Criação de Variáveis**:
   - Cálculo dos dias de atraso (`dias_atraso`).
   - Classificação de cada conta como "Pago", "Em Aberto", "Atrasado", ou "Cancelado".
   - Criação de uma variável binária de inadimplência (1 para inadimplente, 0 para não inadimplente).

3. **Estatísticas por Cliente**:
   - Agregação de dados para calcular o total da dívida, o número de contas vencidas e a média de dias de atraso por cliente.

4. **Modelo de Previsão**:
   - Uso de Regressão Logística para treinar o modelo e prever a inadimplência dos clientes.
   - A métrica de avaliação inclui Acurácia, Matriz de Confusão, Relatório de Classificação e AUC-ROC.

5. **Visualizações**:
   - Gráficos de distribuição de dias de atraso entre clientes inadimplentes e não inadimplentes.
   - Gráfico de dispersão que mostra os dias de atraso dos clientes inadimplentes.

## Requisitos

Para rodar este projeto, é necessário ter os seguintes pacotes Python instalados:

- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`

# Modelo

A regressão logística é ideal para problemas como o de previsão de inadimplência porque:

-É projetada para classificação binária.

-Oferece probabilidades úteis para decisões.

-É simples de interpretar, o que facilita entender o modelo.

-Tem boa performance em dados lineares.

-É eficiente computacionalmente.

# Resultados

O modelo de Regressão Logística foi avaliado com base nas métricas de performance:

Acurácia: 1.0

Matriz de Confusão:

 [[78  0]
 [ 0 15]]
 
Relatório de Classificação:

               precision    recall  f1-score   support

           0       1.00      1.00      1.00        78
           1       1.00      1.00      1.00        15

    accuracy                           1.00        93
   macro avg       1.00      1.00      1.00        93
weighted avg       1.00      1.00      1.00        93

AUC-ROC: 1.0

# Conclusão

O modelo de Regressão Logística foi treinado com sucesso para prever a inadimplência dos clientes da empresa Zero Furo. A intenção é prever a inadimplência de clientes com base em seu comportamento financeiro geral (como total da dívida, quantidade de contas vencidas e média de atraso). A regressão logística deve levar em conta essas variáveis, pois um cliente que pagou, mas ainda tem uma grande dívida ou um histórico de atraso, pode ter maior risco de inadimplência, independentemente da situação atual de uma conta específica.
