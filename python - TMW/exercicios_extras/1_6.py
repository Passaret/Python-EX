# Faça um programa que receba um número em segundos, 
# converta esse número para horas, minuto e segundos. Exemplos:

# Entrada: 556
# Saída: 0:9:16
# 
# Entrada: 140153
# Saída: 38:55:53
#%%
numero = input("Digite um número: ")
numero = int(numero)


horas = numero // 3600
resto_h = numero % 3600
minutos = resto_h // 60
segundos = resto_h % 60


print(f"{horas}:{minutos}:{segundos}")
# %%
