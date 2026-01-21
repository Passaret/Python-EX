#%%
nome_arquivo = "C:/Users/lucas/AQUI PRA CLONAR/Python-EX/python - TMW/dia_07/historia.txt"

# abre arquivo em formato de leitura
open_file = open(nome_arquivo)
# %%
# le os dados do arquivo
conteudo = open_file.read()
print(conteudo)
# %%
# fecha o arquivo
open_file.close()
# %%
# maneira correta de abrir e fechar leitura de arquivos.
with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
print(conteudo)
# %%
