#%%
# Faça um programa que receba 4 alturas usando um laço
# de repetição e realize a soma dessas alturas.

soma = 0
count = 4

while count > 0:
    altura = float(input("Entre com a altura:"))
    soma += altura
    count -= 1
#print("Inseridas e somadas as 4 alturas")
print("A soma das alturas é:", soma)
# %%
