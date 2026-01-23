# Considere a seguinte lista:
# [123, 435, 987, 1984, 2, 19, 423, -178, 320]

# Faça um programa que retorne a posição do menor e do maior valor encontrado:

# O maior valor está na posição x
# O menor valor está na posição y


lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

menor = min(lista)
maior = max(lista)

pos_maior = lista.index(maior)
pos_menor = lista.index(menor)

print(f"\nO maior valor está na posição {pos_maior} \
        \nO menor valor está na posição {pos_menor}")
