# Escreva um programa que solicite ao usuário um nome e uma idade, e crie um dicionário com essas informações. Em seguida, exiba o dicionário.

#%%

dados = dict()


while True:
        nome = input("Digite um nome: ")
        if nome == "":
              break
        idade = input("Digite a idade de {nome}: ")
        dados[nome] = idade
print("\n Dados inseridos: ", dados) 
# %%
