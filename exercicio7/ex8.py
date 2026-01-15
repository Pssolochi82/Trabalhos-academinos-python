#Classe Funcionário
#Crie uma classe `Funcionario` com os seguintes atributos:
#- `nome` (string)
#- `salario` (float)
#- `departamento` (string)
#Implemente os seguintes métodos:
#- `aumentar_salario(percentual)`: aumenta o salário em um percentual
#- `calcular_inss()`: calcula e retorna 11% do salário
#- `calcular_salario_liquido()`: retorna salário - INSS
#- `exibir_info()`: imprime nome, departamento, salário bruto, INSS e salário líquido
#**Teste:** Crie um funcionário com salário de 3000, aumente em 10% e exiba as informações.

class Funcionario:
    def __init__(self, nome, salario, departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento

    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento

    def calcular_inss(self):
        return self.salario * 0.11

    def calcular_salario_liquido(self):
        inss = self.calcular_inss()
        return self.salario - inss

    def exibir_info(self):
        inss = self.calcular_inss()
        salario_liquido = self.calcular_salario_liquido()
        print(f'Nome: {self.nome}')
        print(f'Departamento: {self.departamento}')
        print(f'Salário Bruto: € {self.salario:.2f}')
        print(f'INSS: € {inss:.2f}')
        print(f'Salário Líquido: € {salario_liquido:.2f}')
# Teste
funcionario = Funcionario("Palmira Solochi", 5000.00, "Financeiro")    
funcionario.aumentar_salario(10)
funcionario.exibir_info()
