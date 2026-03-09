import pandas as pd

#data = pd.read_excel('lista.xlsx')
#print(data)

#data = pd.read_excel(r"/Users/gustavojorge/Downloads/Temp/lista.xlsx", sheet_name="Folha2")
print("\n\n\n **** LISTA COMPLETA **** ")
dados = pd.read_excel(r"lista.xlsx", sheet_name="Folha1")
print(dados)

print(" \n **** LISTAR SOMENTE QUE TEM MAIS DE 40 ANOS **** ")

dados_filtrados = dados[dados['Idade'] > 20]
#dados_fich = pd.read_excel('fichas.xlsx')
print(dados_filtrados)

print(" \n **** LISTAR SOMENTE O NOME DOS FORMANDOS **** ")
dados_fich = pd.DataFrame(dados, columns=['Nome_formandos'])
print(dados_fich)


