#%%
# Faça um programa que receba 4 alturas usando um laço
# de repetição e realize a soma dessas alturas.

soma = 0
for i in range(4):
    altura = input("Digite sua altura (use . como separador)")
    altura = float(altura)
    soma += altura

print(f"A soma das alturas é: {soma}")


#%%
# Exercicio com while
# soma = 0
# count = 4

# while count > 0:
#     altura = float(input("Entre com a altura:"))
#     soma += altura
#     count -= 1
# print("A soma das alturas é:", soma)
#