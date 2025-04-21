# Faça um programa que receba um número inteiro
# e calcule sua raiz quadrada e exiba o resultado.

numero = input("Entre com um número inteiro para calcular sua raiz quadrada: ")

raiz = int(numero)** (1/2)
raiz = round(raiz, 4)

print("Raiz quadrada de", numero, "é:", raiz)