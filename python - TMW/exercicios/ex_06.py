# Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista: 
# laranja, cerveja, miojo, carvão, picanha.
#%%
lista = ['laranja', 'cerveja', 'miojo', 'carvao', 'picanha']

item_compra = input("Digite o nome do item que você deseja comprar (SEM ACENTOS): ")
item_compra = item_compra.lower()


if item_compra in lista:
    print('O item que você deseja comprar está na lista')
else:
    print('O item que você deseja comprar não está na lista')