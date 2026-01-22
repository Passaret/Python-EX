# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra
palavra = input("Escreve uma palavra: ")

count = 0

for i in palavra:
    if i == "a":
        count += 1
    else:
        continue
print("Palavra: ", palavra.upper(), "\nQuantidades de letra A: ", count)
