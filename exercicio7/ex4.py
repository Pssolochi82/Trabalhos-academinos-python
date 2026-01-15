#Classe Produto com Estoque
#Crie uma classe `Produto` com os seguintes atributos:
#- `nome` (string)
#- `preco` (float)
#- `quantidade_estoque` (inteiro)
#Implemente os seguintes métodos:
#- `adicionar_estoque(quantidade)`: aumenta o estoque
#- `remover_estoque(quantidade)`: diminui o estoque (verifica se há quantidade suficiente)
#- `calcular_valor_total()`: retorna preco × quantidade_estoque
#- `exibir_info()`: imprime as informações do produto com saldo total
#**Teste:** Crie um produto, adicione 50 unidades, remova 15, adicione 20
#novamente e exiba as informações.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = 0

    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade

    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade_estoque:
            self.quantidade_estoque -= quantidade
        else:
            print("Quantidade insuficiente em estoque.")

    def calcular_valor_total(self):
        return self.preco * self.quantidade_estoque

    def exibir_info(self):
        valor_total = self.calcular_valor_total()
        print(f'Produto: {self.nome}')
        print(f'Preço: R$ {self.preco:.2f}')
        print(f'Quantidade em estoque: {self.quantidade_estoque}')
        print(f'Valor total em estoque: R$ {valor_total:.2f}')
# Teste
produto = Produto("Caneta", 2.50)
produto.adicionar_estoque(50)
produto.remover_estoque(15)
produto.adicionar_estoque(20)
produto.exibir_info()
