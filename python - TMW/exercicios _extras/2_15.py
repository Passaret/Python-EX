#Escreva um programa que receba uma lista de números
#  do usuário e conte quantas vezes um número
#  específico aparece na lista.
#  Solicite ao usuário um número e exiba a contagem.

#%%
lista = [1,2,3,3,2,1,1,1,1,5,6,7,7,6,5]

numero = input("Entre com um número: ")
numero = int(numero)

count = 0
for i in lista:
    if i == numero:
        count += 1

print("quantidade de", numero, ":", count)
# %%
