# Faça um programa que receba um número. Este número corresponde a uma posição na sequência de Fibonacci: 1, 1, 2, 3, 5,...

# Exiba o número da sequência cuja posição foi informada:
# 	A posição x corresponde ao número y

def user_input():
    while True:
        try:
            user_input = int(input("Entre com um número inteiro: "))
        except ValueError as err:
            print("Entre com um número válido!")
            continue
        if user_input >= 0:
            return(user_input)
        print("Entre com um número >= 0")

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)
    
num = user_input()

print(f"Fibonacci de {num} é {fibo(num)}")

