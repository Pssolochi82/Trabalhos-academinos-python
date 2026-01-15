#Classe Jogador
#Crie uma classe `Jogador` com os seguintes atributos:
#- `nome` (string)
#- `vida` (inteiro, começando em 100)
#- `energia` (inteiro, começando em 100)
#Implemente os seguintes métodos:
#- `atacar(outro_jogador, dano=10)`: reduz a vida do outro jogador em `dano` unidades
#- `usar_energia(quantidade)`: reduz a energia em `quantidade` unidades (não pode ser negativa)
#- `recuperar_energia(quantidade)`: aumenta a energia em `quantidade` unidades - `exibir_status()`: imprime nome, vida e energia atuais
#- `verificar_derrota()`: retorna True se vida ≤ 0
#**Teste:** Crie dois jogadores, façam ataques mútuos, recuperem energia e verifique o status final.

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.energia = 100

    def atacar(self, outro_jogador, dano=10):
        outro_jogador.vida -= dano
        if outro_jogador.vida < 0:
            outro_jogador.vida = 0

    def usar_energia(self, quantidade):
        self.energia -= quantidade
        if self.energia < 0:
            self.energia = 0

    def recuperar_energia(self, quantidade):
        self.energia += quantidade
        if self.energia > 100:
            self.energia = 100

    def exibir_status(self):
        print(f'Nome: {self.nome}')
        print(f'Vida: {self.vida}')
        print(f'Energia: {self.energia}')

    def verificar_derrota(self):
        return self.vida <= 0
# Teste
jogador1 = Jogador("Herói")
jogador2 = Jogador("Vilão")
jogador1.atacar(jogador2, dano=15)
jogador2.atacar(jogador1, dano=20)
jogador1.usar_energia(30)
jogador2.recuperar_energia(20)
jogador1.exibir_status()
jogador2.exibir_status()
if jogador1.verificar_derrota():
    print(f'{jogador1.nome} foi derrotado!')
if jogador2.verificar_derrota():
    print(f'{jogador2.nome} foi derrotado!')
    