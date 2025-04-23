#%%
# Faça um programa que receba 4 alturas usando um laço
# de repetição e realize a soma dessas alturas.

soma = 0
for i in range(4):
    altura = input("Digite sua altura (use . como separador)")
    altura = float(altura)
    soma += altura

print(f"A soma das alturas é: {soma}")
