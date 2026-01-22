# Faça um programa que receba um número. Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:

# 	O número x é impar
# ou
# 	O número x é par

def get_input():
    while True:
        try:
            numero = int(input("Insira um número? "))
        except ValueError as err:
            print("Insira uma número válido!")
            continue
        if numero is not int:
            return(numero)
        print("Insira um número!")


def par(x:int):
    if x % 2 == 0:
        print("O número ", x ," é par")
    else:
        print("O número ", x ," é impar")

par(get_input())


# %%
