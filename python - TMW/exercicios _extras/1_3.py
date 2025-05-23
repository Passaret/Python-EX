# Faça um programa que receba o raio de uma circunferência em centímetros. 
# Retorne para o usuário qual é a área e perímetro desta circunferência 
# no seguinte formato.

#Área:  x.xx
#Perímetro:  y.yy

#%%

raio = input("Digite o raio da circunferência (em cm): ")
raio = float(raio)

area = round((3.14 * (raio)**2), 3)
perimetro = round((2 * 3.14 * raio), 3)

print(f"A área da circunferência é: {area}\
        O perímetro da circunferência é: {perimetro}")

