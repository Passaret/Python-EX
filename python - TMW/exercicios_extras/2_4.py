# Faça um programa que receba 4 notas de um aluno. Retorne a média dessas notas, a menor e a maior nota:

# Média: x
# Menor: y
# Maior: z

def notas_input():
    notas = []
    while len(notas) < 4:
        try:
            nota = int(input("Digite a nota do aluno: "))
        
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("A nota deve ser entre 0 e 10")
        
        except ValueError:
            input("Digite um valor númerico!")
        
    return(notas)

valores = notas_input()

media = sum(valores)/len(valores)
menor = min(valores)
maior = max(valores)

print(f"\nMédia: {media} \
        \nMenor: {menor} \
        \nMaior: {maior}")


