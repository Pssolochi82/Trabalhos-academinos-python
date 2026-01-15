#Classe Conta Bancária (Avançada)
#Crie uma classe `ContaBancaria` com os seguintes atributos:
#- `numero_conta` (string)
#- `titular` (string)
#- `saldo` (float)
#- `tipo_conta` (string: "Corrente" ou "Poupança")
#- `historico` (lista de operações)
#Implemente os seguintes métodos:
#- `depositar(valor)`: adiciona valor ao saldo e regista no histórico
#- `sacar(valor)`: subtrai valor do saldo (se houver saldo) e regista no histórico
#- `transferir(outra_conta, valor)`: transfere valor para outra conta e regista em ambos os históricos
#- `exibir_historico()`: imprime todas as operações realizadas
#- `exibir_saldo()`: imprime o saldo atual
#**Teste:** Crie duas contas, realize depósitos, saques e uma transferência. Exiba o histórico de ambas.

class ContaBancaria:    
    def __init__(self, numero_conta, titular, tipo_conta):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0.0
        self.tipo_conta = tipo_conta
        self.historico = []

    def depositar(self, valor):
        self.saldo += valor
        self.historico.append(f'Depósito: € {valor:.2f}')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f'Saque: € {valor:.2f}')
        else:
            print("Saldo insuficiente para saque.")

    def transferir(self, outra_conta, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            outra_conta.saldo += valor
            self.historico.append(f'Transferência para {outra_conta.numero_conta}: € {valor:.2f}')
            outra_conta.historico.append(f'Transferência de {self.numero_conta}: € {valor:.2f}')
        else:
            print("Saldo insuficiente para transferência.")

    def exibir_historico(self):
        print(f'Histórico da conta {self.numero_conta}:')
        for operacao in self.historico:
            print(operacao)

    def exibir_saldo(self):
        print(f'Saldo atual da conta {self.numero_conta}: € {self.saldo:.2f}')
# Teste
conta1 = ContaBancaria("12345-6", "Palmira Solochi",
                        "Corrente")
conta2 = ContaBancaria("65432-1", "Délcia Melo",
                        "Poupança")
conta1.depositar(5000)
conta1.sacar(1000)
conta1.transferir(conta2, 500)
conta1.exibir_saldo()
conta2.exibir_saldo()
conta1.exibir_historico()
conta2.exibir_historico()

