import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC16ef4c8a0dbec65c8b724c6e837e124c"
# Your Auth Token from twilio.com/console
auth_token  = "58ae28cb8b71d61a93f0491a974eae85"
client = Client(account_sid, auth_token)

# Passo a passo da solução

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
     tabela_vendas = pd.read_excel(f'{mes}.xlsx')
     if (tabela_vendas['Vendas'] > 55000).any():
         vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
         vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
         print(f' No mês de mês de {mes}, o Vendedor : {vendedor}, vendeu: R${vendas}, e bateu a meta')
         message = client.messages.create(
             to="+5511951678649",
             from_="+15134492362",
             body=f' No mês de mês de {mes}, o Vendedor : {vendedor}, vendeu: R${vendas}, e bateu a meta')

         print(message.sid)


# Para cada arquivo:

# Verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Enviar um SMS com o nome, o mês e as vendas do vendedor

# Para isso usamos a Library Twilio e criamos uma conta.

# Caso não seja maior do que 55.000 não quero fazer nada