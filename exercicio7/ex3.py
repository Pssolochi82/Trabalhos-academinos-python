#Classe Estudante
#Crie uma classe `Estudante` com os seguintes atributos:
#- `nome` (string)
#- `matricula` (string)
#- `notas` (lista de números)
#Implemente os seguintes métodos:
#- `adicionar_nota(nota)`: adiciona uma nota à lista de notas
#- `calcular_media()`: retorna a média aritmética das notas
#- `verificar_aprovacao()`: retorna True se a média ≥ 10, False caso contrário
#- `exibir_status()`: imprime nome, matrícula, média e status de aprovação
#**Teste:** Crie um estudante, adicione 4 notas (12, 14, 9, 11) e exiba o status.

class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        return self.calcular_media() >= 10

    def exibir_status(self):
        media = self.calcular_media()
        status = "Aprovado" if self.verificar_aprovacao() else "Reprovado"
        print(f'Nome: {self.nome}')
        print(f'Matrícula: {self.matricula}')
        print(f'Média: {media:.2f}')
        print(f'Status: {status}')
# Teste
estudante = Estudante("Ana Silva", "2023001")   
estudante.adicionar_nota(12)
estudante.adicionar_nota(14)
estudante.adicionar_nota(9)
estudante.adicionar_nota(11)
estudante.exibir_status()
