#Escreva um programa que solicite ao usuário frases. 
# Para parar de solicitar frases, ele pode apenas apertar o “enter”.
#Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.

dicionario = dict()

while True:
    frase = input("Digite a frase que quiser, aperte enter quando quiser parar").lower()
    if frase == "":
        break
    if frase not in dicionario:
        dicionario[frase] = 1
    elif frase in dicionario:
        dicionario[frase] += 1


        
items = list(dicionario.items())
items.sort(key = lambda x: x[-1], reverse=True)

for i,j in dicionario.items():
    print(f"{i} -> {j}")
