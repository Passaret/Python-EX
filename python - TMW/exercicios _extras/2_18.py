#%%
#Escreva um programa que solicite ao usuário frases. 
# Para parar de solicitar frases, ele pode apenas apertar o “enter”.
#Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.

dic = {}

while True:
    frase = input("Digite sua frase: ")
    if frase == "":
        break
    if frase not in dic:
        dic[frase] = 1
    else:
        dic[frase] += 1

items = list(dic.items())
items.sort(key = lambda x: x[-1], reverse= True)

for i,j in items:
    print(i, '->', j)
# %%
