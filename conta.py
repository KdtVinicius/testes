class SaldoInsuficienteException(Exception):
    pass

class Conta:
    def __init__(self, numero, agencia, saldo):
        if saldo < 0:
            raise ValueError("Saldo inicial não pode ser negativo")

        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo

    def depositar(self, valor):
        if valor < 0:
            raise ValueError("Valor de depósito deve ser positivo")

        self.saldo += valor

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("Valor de saque deve ser positivo")

        if valor > self.saldo:
            raise SaldoInsuficienteException("Saldo insuficiente para saque")

        self.saldo -= valor

    def saldo(self):
        return self.saldo
