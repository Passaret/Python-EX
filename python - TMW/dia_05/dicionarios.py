#%%

lista = [2, 132, 'teo', ['ds', 'de', 'da'], True]

lista[2]
# %%
# dicionário
# pares de chave/valor

dados_teo = {
    'sobrenome':'Calvo',
    'nome': 'Téo',
    'filhos': True,
    'formacao': ['estatistica', 'bigdata datascience'],
    'cargos': [
        {'nome': 'ds jr.', 'empresa': 'tapps'},
        {'nome': 'ds pl.', 'empresa': 'sas'},
        {'nome': 'ds sr.', 'empresa': 'boticario'},
        {'nome': 'ds spec.', 'empresa': 'via varejo'},
        ]
    }

print(dados_teo)
# %%
print((dados_teo['nome']))
print((dados_teo['formacao'][-1]))
print((dados_teo['cargos'][-1]['empresa']))
# %%
dados_teo['estado civil'] = 'casado'
print(dados_teo)
# %%
print('Chaves:', dados_teo.keys())
print('Valores:', dados_teo.values())
print('Items:', dados_teo.items())
# %%
for i in dados_teo:
    print(i, "->", dados_teo[i])
# %%
for chave, valor in dados_teo.items():
    print(chave, "->", valor)
    
# %%
