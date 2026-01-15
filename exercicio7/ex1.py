#1: Classe Livro Crie uma classe `Livro` com os seguintes atributos:
#- `titulo` (string)
#- `autor` (string)
#- `paginas` (inteiro)
#Implemente um método `descricao()` que retorna uma string formatada com as informações do livro no formato:
#"[Titulo] escrito por [Autor] com [Paginas] páginas"`
#**Teste:** Crie dois objetos Livro e chame o método descricao() para cada um.

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def descricao(self):
        return f'"{self.titulo}" escrito por {self.autor} com {self.paginas} páginas'
# Teste
livro1 = Livro("1984", "George Orwell", 328)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1216)
print(livro1.descricao())
print(livro2.descricao())
