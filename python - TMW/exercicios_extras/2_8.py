# 2.4 Faça um programa que receba 4 notas de um aluno. Retorne a média dessas notas, a menor e a maior nota:

# Média: x
# Menor: y
# Maior: z

# Refaça o exercício 2.4 utilizando for e listas para receber as notas dos alunos


def notas_input():
    while True:
        try:
            nota = int(input("Digite a nota do aluno: "))
        except ValueError as err:
            input("Digite uma nota válida!")
        if 0 <= nota <= 10:
            return(nota)

notas = []
for i in range(4):
    nota = notas_input()
    notas.append(nota)

media = sum(notas)/len(notas)
menor = min(notas)
maior = max(notas)

print(f"\nMédia: {media} \
        \nMenor: {menor} \
        \nMaior: {maior}")

