#: Classe Retângulo
#Crie uma classe `Retangulo` com os seguintes atributos:
#- `largura` (float)
#- `altura` (float)
#Implemente os seguintes métodos:
#- `calcular_area()`: retorna largura × altura
#- `calcular_perimetro()`: retorna 2 × (largura + altura)
#- `exibir_dimensoes()`: imprime largura, altura, área e perímetro
#**Teste:** Crie um retângulo com largura 10 e altura 5, depois exiba as dimensões.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

    def exibir_dimensoes(self):
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()
        print(f'Largura: {self.largura}')
        print(f'Altura: {self.altura}')
        print(f'Área: {area}')
        print(f'Perímetro: {perimetro}')
# Teste
retangulo = Retangulo(10, 5)
retangulo.exibir_dimensoes()
#