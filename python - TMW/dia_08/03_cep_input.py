#%%
import requests # para realizar requisições na web
import json # para tratar json de listas/dicionarios para arquivos json


#%%
ceps = int(input("Entre com um CEP:"))

url = "https://viacep.com.br/ws/{cep}/json"

resposta = requests.get(url.format(cep = ceps))

dados= dict()
if resposta.status_code == 200:
    dados = resposta.json()

for chave, valor in dados.items():
    print(chave, "->", valor)

# %%
