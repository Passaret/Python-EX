# Escreva um programa que solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

numero = int(input("Escolha um número: "))

for i in range(11):
    print(f"{numero} X {i} = {numero * i}")


