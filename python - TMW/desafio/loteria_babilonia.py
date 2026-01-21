# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

import random
numero_sorteio = random.randint(1,15)


def get_input():
        while True:
            try:
                numero_usuario = int(input("Entre com um número: "))

            except ValueError as err:
                print("\nValor inválido! Entre com um número inteiro entre 1 e 15\n")
                continue

            if 1 <= numero_usuario <= 15:
                return(numero_usuario)
            print("\nValor inválido! O valor deve ser entre 1 e 15\n")

def check_numbers(sorteio, usuario):
    if sorteio == usuario:
        print("\nParabéns! Você venceu!")
        return True
    elif usuario > sorteio:
        print("\nPalpite errado! Tente um Número menor!")
        return False
    else:
        print("\nPalpite errado!! Tente um Número maior!")
        return False

for i in range(3):
    numero_usuario = get_input()
    if check_numbers(sorteio=numero_sorteio, usuario=numero_usuario):
        break
    if i != 2:
        print("Tentativas restantes:", 2-i, "\n")
else:
    print("Suas tentativas acabaram!! \n" \
    "\nO número correto era:", numero_sorteio)