import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC052fabea239b03878763de2b671df30d"
# Your Auth Token from twilio.com/console
auth_token  = "d846cd7c8b3d68ebc307476182249fc8"
client = Client(account_sid, auth_token)


#Abrir os 6 arquivos em excel:
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}.')
        message = client.messages.create(
            to="+5585988920125",
            from_="+15342484058",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

