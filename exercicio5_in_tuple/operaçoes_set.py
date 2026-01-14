# Utilizando a instrução SET faça as seguintes operações:
#a. Adicione 5 países
#b. Liste os países
#c. Remova um país a sua escolha
#d. Insira um país já existente
#e. Imprima os países e o número de países existentes

# a. Adicione 5 países
paises = set()
paises.add("Brasil")
paises.add("Argentina")
paises.add("Moçambique")
paises.add("Angola")
paises.add("Portugal")
# b. Liste os países
print("Países adicionados:", paises)
# c. Remova um país a sua escolha
paises.remove("Portugal")
# d. Insira um país já existente
paises.add("Brasil")  # Brasil já existe no conjunto
# e. Imprima os países e o número de países existentes
print("Países após remoção e tentativa de adição de existente:", paises)
print("Número de países existentes:", len(paises))

