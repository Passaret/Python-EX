# Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

#%%
nome = input("Digite seu nome completo")
nome= nome.lower()

if 'calvo' in nome and 'silva' in nome:
    print('Você é da família Calvo e da família Silva')
elif 'calvo' in nome:
    print("Você é da família Calvo")
elif 'silva' in nome:
    print('Você é da família Silva')
else:
    print("Você não é da família Calvo nem da família Silva")
# %%
