# Faça um programa que receba o nome e a idade de uma pessoa. 

# Caso essa pessoa tenha menos de 18 anos, exiba o aviso:
# 	“Fulano, você não pode dirigir nem beber”

# Para as pessoas entre 18 e 65 anos, exiba o aviso:
# 	“Fulano, bebida liberada! Só não vale dirigir!”

# Para as pessoas com mais de 65 anos, exiba o aviso:
# 	“Fulano, beba com muita moderação!”

nome = input("Qual o seu nome? ")

def get_input():
    while True:
        try:
            idade = int(input("Quantos anos você tem? "))
        except ValueError as err:
            print("Insira uma idade válida!")
            continue
        if idade > 0:
            return(idade)
        print("Insira um número inteiro!")


def func(y:int):
    if y < 18:
        print(nome, ", você não pode dirigir nem beber")
    if 18 <= y <= 65:
        print(nome, ", bebida liberada! Só não vale dirigir!")
    else:
        print(nome, ", beba com muita moderação!")

func(get_input())
