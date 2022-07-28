# Consumindo a API de cotações de moedas
import requests
import json 

# get = pega as informações da API
cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']['bid']
# print(cotacoes)
print(cotacao_dolar)



