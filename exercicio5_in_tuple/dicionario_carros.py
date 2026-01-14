# Faça um dicionário de dados sobre automóveis. Exemplo: Marca “BMW”, Modelo “i3”. Realize as seguintes operações:
#a. Crie um dicionário com pelo menos 5 marcas de automóveis e os respetivos modelos.
#b. Liste o dicionário.
#c. Crie um novo elemento ao dicionário para uma mesma marca.
#d. Volte a listar.


carros = {
    "BMW": "i3",
    "Audi": "A4",
    "Toyota": "Corolla",
    "Ford": "Mustang",
    "Honda": "Civic"
    
}
# b. Liste o dicionário.
print("Dicionário inicial de carros:", carros)
# c. Crie um novo elemento ao dicionário para uma mesma marca.
carros["BMW"] = "X5"  # Adicionando um novo modelo para a marca BMW
# d. Volte a listar.
print("Dicionário após adicionar novo modelo para BMW:", carros)

