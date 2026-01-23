# Escreva um programa que solicite ao usuário uma palavra e verifique se a palavra é um palíndromo 
# (ou seja, é a mesma palavra quando lida de trás para frente).

palavra = input("Escolha uma palavra: ")

if palavra == palavra[::-1]:
    print(f"{palavra} É uma palavra palíndromo")
else:
    print(f"{palavra} NÃO é uma palavra palíndromo")