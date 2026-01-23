# Faça um programa que receba um número. Verifique se este número é primo ou não, e retorne o resultado:
# 	O número x é primo
# 	O número x não é primo

#%%
num_input = int(input("Insira um número: "))

def primo(x):
    if x < 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

if primo(num_input):
    print(f"{num_input} é primo!")
else:
    print(f"{num_input} não é primo!")
