"""Você trabalha em uma empresa de telecom e tem clientes de vários serviços
diferentes, entre os principais: internet e telefone.
O problema é que, analisando o histórico dos clientes dos últimos anos,
você percebeu que a empresa está com Churn de mais de 26% dos clientes.
Isso representa uma perda de milhões para a empresa.

O que a empresa precisa fazer para resolver isso?"""

#Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing
#Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset"


"""Passo 1: Importar as bases de dados da empresa."""
import pandas as pd
import plotly.express as px


tabela = pd.read_csv(r"C:\Users\Objectedge\Downloads\telecom_users.csv")


"""Passo 2: Visualizar as bases de dados."""
" Entender quais as informações que temos e descobrir os erros"

# Deletamos uma coluna que não era útil ao nosso projeto.
tabela = tabela.drop("Unnamed: 0", axis=1) #axis = 0 -> linha axis = 1 -> coluna


"""Passo 3: Tratamento de dados."""


# Convertemos uma coluna que estava como texto em numerica e forçamos
# os erros se tornarem numéricos, diminuindo alguns dados.
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")


"""Tratando colunas completamente vazias"""
# Deletando todas as colunas onde os valores são vazios
tabela = tabela.dropna(how = "all", axis = 1)


"""Tratando linhas com pelo menos um valor vazio"""
# Deletando todas as linhas onde alguns valores são vazios
tabela = tabela.dropna(how = "any", axis = 0)


"""Passo 4: Análise Inicial (entender como estão os cancelamentos)"""
# Trouxemos a coluna Churn pra sabermos quantos cancelaram, e também a porcentagem disso.
"""print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))"""


"""Passo 5: Análise Completa (entender o motivo do cancelamento)"""
# Como cada coluna da nossa base de dados, impacta o cancelamento
# Usaremos o plotly, usando o histograma como gráfico

for coluna in tabela.columns:
    # Criando o gráfico
    grafico = px.histogram(tabela, x = coluna, color="Churn", text_auto=True )
    # Exibindo o gráfico
    grafico.show()

""" Conclusões e Ações:
- A chance do cliente cancelar nos primeiros meses é muito alta.
Solução: oferecer algum desconto ou algo que beneficie o cliente nos primeiros meses (de 3 a 12 meses)

- Clientes com famílias maiores, tendem a cancelar menos
Solução: oferecer segunda linha com desconto ou até de graça dependendo do perfil.

- Problemas nos serviços de fibra. Taxa de cancelamento muito alta. 

- Quanto mais serviços o cliente tem, menor a chance dele cancelar.
Solução: oferecer serviços com desconto, ou de grátis conforme plano e perfil do cliente.

- Quase todos os cancelamentos estão  no plano mensal
Solução: buscar oferecer alguma vantagem no plano mensal, desconto ou melhorar a forma de pagar.

- Boleto tem muito mais cancelamento do que as outras formas
Solução: Ofertar desconto nas outras formas de pagamento ou oferecer outro método no boleto.
"""