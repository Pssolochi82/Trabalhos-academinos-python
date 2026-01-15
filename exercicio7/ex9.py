#Classe Biblioteca
#Crie uma classe `Biblioteca` com o seguinte atributo:
#- `livros` (lista de objetos Livro - reutilize a classe do Exercício 1)
#Implemente os seguintes métodos:
#- `adicionar_livro(livro)`: adiciona um livro à biblioteca
#- `remover_livro(titulo)`: remove um livro pelo título
#- `buscar_livro(titulo)`: retorna o livro se encontrado, None caso contrário
#- `listar_todos()`: imprime todos os livros na biblioteca
#- `contar_livros()`: retorna a quantidade de livros
#**Teste:** Crie uma biblioteca, adicione 3 livros, busque um por título, remova um e liste todos.

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def descricao(self):
        return f'"{self.titulo}" escrito por {self.autor} com {self.paginas} páginas'
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                return
        print("Livro não encontrado.")

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None

    def listar_todos(self):
        for livro in self.livros:
            print(livro.descricao())

    def contar_livros(self):
        return len(self.livros)
# Teste
biblioteca = Biblioteca()
livro1 = Livro("1984", "George Orwell", 328)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1216)
livro3 = Livro("Dom Casmurro", "Machado de Assis", 352)
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
encontrado = biblioteca.buscar_livro("1984")
if encontrado:
    print("Livro encontrado:", encontrado.descricao())
biblioteca.remover_livro("O Senhor dos Anéis")
print("Livros na biblioteca:")
biblioteca.listar_todos()
print("Total de livros:", biblioteca.contar_livros())
