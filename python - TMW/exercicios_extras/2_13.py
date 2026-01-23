# Faça um programa que receba um número e exiba seu fatorial.


numero = int(input("Insira um número: "))

def func_fatorial(x):
    if x < 0:
        print("Não existe fatorial de negativo")
    elif x <= 1:
        1
    else:
        fatorial = 1
        for i in range(1, x + 1):
            fatorial *= i
        return(fatorial)
    
func_fatorial(numero)
