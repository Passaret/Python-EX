#%%
idades = [28, 42, 43, 35, 39, 28, 38, 42, 34]

print(idades)
# %%
teo = ['Téo', 'Calvo', 32, 1, 'Casado', 2342.98]
print(teo)
#%%
type(teo)
# %%
# idade
teo[2]

#renda
print(teo[5])
# %%
print("soma idades:", sum(idades))

print('qtde idades:', len(idades))

print('media idades:', sum(idades)/len(idades))

print("menor idade:", min(idades))

print("menor idade:", max(idades))
# %%

teo = ['Téo Calvo', 32, 
       True, 'Casado',
       ['estagiario', 'ds jr', 'ds pl', 'ds sr.', 'head'],
       [1500, 4000, 4550, 6500, 10000],
       ['Ana', "Maria", "Claudia"]]

print("Tamanho Teo:", len(teo))

teo[-1][-2]
# %%
print(teo[0:4])
print(teo[:4])

print(teo[4][3:])
print(teo[4][-2:])
# %%
salarios = teo[5]
salarios[::-1]
# %%
