#Escreva um programa que receba uma lista de números
#  do usuário e conte quantas vezes um número
#  específico aparece na lista.
#  Solicite ao usuário um número e exiba a contagem.

#%%

lista = []
user_input = input("Insira quanto números quiser separando por virgula").split(",")

for i in user_input:
    lista.append(i)

numero = input("Entre com um número: ")

count = 0
for i in lista:
    if i == numero:
        count += 1

print("quantidade de", numero, ":", count)
# %%
