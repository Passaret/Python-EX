# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)

#%%
sorvete = """"
SORVETE:
(1) Casquinha - R$ 1,00
(2) Cascão - R$ 2,50
(3) Cestinha - R$ 4,00
"""
sabor = """
SABOR DO SORVETE:
(1) Morango
(2) Creme
(3) Chocolate
"""
cobertura = """
COBERTURA:
(1) Caramelo - R$ 1,50
(2) Morango - R$ 1,50
(3) Chocolate - R$ 1,50
(4) Sem cobertura - R$ 0,00
"""

sorvete_dic = {1:'Casquinha', 2:"Cascão", 3:'Cestinha'}
sabor_dic = {1:"Morango", 2:"Creme", 3:"Chocolate"}
cobertura_dic = {1:"Caramelo", 2:"Morango", 3:"Chocolate", 4:"Sem cobertura"}

opcao_sorvete = input(sorvete)
opcao_sabor = input(sabor)
opcao_cobertura = input(cobertura)

try:
    opcao_sorvete_int = int(opcao_sorvete)
    opcao_sabor_int = int(opcao_sabor)
    opcao_cobertura_int = int(opcao_cobertura)
except ValueError:
    print("Erro: Insira apenas números válidos.")
    exit()

erros = False

if opcao_sorvete_int not in sorvete_dic:
    print("Sorvete inválido!")
    erros = True

if opcao_sabor_int not in sabor_dic:
    print("Sabor inválido!")
    erros = True

if opcao_cobertura_int not in cobertura_dic:
    print("Cobertura inválida!")
    erros = True

# Se houver qualquer erro, finaliza o programa
if erros:
    print("\nPor favor, reinicie o pedido com opções válidas.")
    exit()

if opcao_sorvete == "1":
    valor_sorvete = 1

elif opcao_sorvete == "2":
    valor_sorvete = 2.5

elif opcao_sorvete == "3":
    valor_sorvete = 4


if opcao_cobertura == "4":
    valor_cobertura = 0
else:
    valor_cobertura = 1.5   

valor_total = valor_sorvete + valor_cobertura
print("\nPedido realizado com sucesso:")
print("Sorvete:", sorvete_dic[opcao_sorvete_int], "\nSabor:", sabor_dic[opcao_sabor_int], "\nCobertura:", cobertura_dic[opcao_cobertura_int])
print("\nValor final: R$", valor_total)
# %%
