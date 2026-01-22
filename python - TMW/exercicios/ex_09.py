#%%
# Faça um programa que receba uma quantidade indefinida
# de valores correspondentes a “saldo em conta”,
# mas quando o usuário apertar “enter” sem digitar valor algum,
# o programa para de receber valores, e exibe a soma
# de todos os valores digitados anteriormente.

saldo_total = 0

while True:
    valor = input("Valor desejado (pressione ENTER para terminar)")
    if valor == "":
        break
    try:
        saldo_total += float(valor)
    except ValueError:
        print('Valor inválido. Digite um número válido')
print(f"A saldo_total dos valores digitados é: {saldo_total}")
