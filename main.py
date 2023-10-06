from typing import List

class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'>>> Codigo {self.codigo} Saldo {self.saldo} <<<'


def deposito_para_todos(contas):
    for conta in contas:
        conta.depositar(100)


conta_um = ContaCorrente(15617)
conta_um.depositar(500)

conta_dois = ContaCorrente(59845)
conta_dois.depositar(1000)

conta_tres = ContaCorrente(82643)
conta_tres.depositar(700)

contas = [conta_um, conta_dois, conta_tres]

print(contas[0], contas[1], contas[2])
deposito_para_todos(contas)
print(contas[0], contas[1], contas[2])