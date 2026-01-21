import requests # para realizar requisições na web
import json # para tratar json de listas/dicionarios para arquivos json


#%%
ceps = int(input("Entre com um CEP:"))

url = "https://viacep.com.br/ws/{cep}/json"

dados = []

resposta = requests.get(url.format(cep = ceps))

if resposta.status_code == 200:
    print(resposta.json())
