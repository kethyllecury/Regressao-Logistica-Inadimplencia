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

--É projetada para classificação binária.
--Oferece probabilidades úteis para decisões.
--É simples de interpretar, o que facilita entender o modelo.
--Tem boa performance em dados lineares.
--É eficiente computacionalmente.

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

# Resultado dos Inadimplentes

             id  situacao vencimento     valor  ...                       hoje  dias_atraso situacao_atual inadimplente
2   20715622393         1 2020-12-28    350.00  ... 2025-03-01 13:13:25.949720         1524           Pago            1
4   20715622265         1 2021-06-10   3500.00  ... 2025-03-01 13:13:25.949720         1360           Pago            1
5   20715623554         1 2021-11-01  10150.00  ... 2025-03-01 13:13:25.949720         1216           Pago            1
6   20715623522         1 2021-10-27    800.00  ... 2025-03-01 13:13:25.949720         1221           Pago            1
7   20715623941         1 2021-10-01   3225.30  ... 2025-03-01 13:13:25.949720         1247           Pago            1
8   20715623163         1 2022-03-22    400.00  ... 2025-03-01 13:13:25.949720         1075           Pago            1
9   20715624022         1 2022-10-05  11764.18  ... 2025-03-01 13:13:25.949720          878           Pago            1
10  20715624051         1 2022-11-07  13750.00  ... 2025-03-01 13:13:25.949720          845           Pago            1
11  20715624025         1 2022-10-17  15400.00  ... 2025-03-01 13:13:25.949720          866           Pago            1
16  20715623866         1 2023-04-14  19800.00  ... 2025-03-01 13:13:25.949720          687           Pago            1
17  20715622770         1 2023-05-05   3000.00  ... 2025-03-01 13:13:25.949720          666           Pago            1
22  20715622755         1 2023-05-05    666.67  ... 2025-03-01 13:13:25.949720          666           Pago            1
26  20715622808         1 2023-09-05    666.65  ... 2025-03-01 13:13:25.949720          543           Pago            1
27  20715623006         1 2023-03-17    500.00  ... 2025-03-01 13:13:25.949720          715           Pago            1
34  20715622934         1 2023-09-08   4228.00  ... 2025-03-01 13:13:25.949720          540           Pago            1
35  20715623226         1 2023-09-25  13160.00  ... 2025-03-01 13:13:25.949720          523           Pago            1
36  20715623170         1 2024-01-25   5040.00  ... 2025-03-01 13:13:25.949720          401           Pago            1
37  20715622957         1 2023-12-15   7250.00  ... 2025-03-01 13:13:25.949720          442           Pago            1
39  20715622643         1 2024-05-27   8880.00  ... 2025-03-01 13:13:25.949720          278           Pago            1
40  20715626423         1 2024-05-06    288.00  ... 2025-03-01 13:13:25.949720          299           Pago            1
41  20715622699         2 2024-07-03   1908.00  ... 2025-03-01 13:13:25.949720          241      Em Aberto            1
42  20715622168         1 2024-07-08    743.76  ... 2025-03-01 13:13:25.949720          236           Pago            1
43  20715622715         1 2024-07-08    508.80  ... 2025-03-01 13:13:25.949720          236           Pago            1
44  20715621862         2 2024-07-22   2426.66  ... 2025-03-01 13:13:25.949720          222      Em Aberto            1
45  20715626640         2 2024-06-17    424.00  ... 2025-03-01 13:13:25.949720          257      Em Aberto            1
46  20715625843         2 2024-07-18   1190.00  ... 2025-03-01 13:13:25.949720          226      Em Aberto            1
47  20715625851         2 2024-07-18   1190.00  ... 2025-03-01 13:13:25.949720          226      Em Aberto            1
48  20715625857         2 2024-07-18   1190.00  ... 2025-03-01 13:13:25.949720          226      Em Aberto            1
49  20715625863         2 2024-07-18   1190.00  ... 2025-03-01 13:13:25.949720          226      Em Aberto            1
50  20715625867         2 2024-07-18   1190.00  ... 2025-03-01 13:13:25.949720          226      Em Aberto            1
