import unittest
from conta.py import Conta, SaldoInsuficienteException

class TestContaCriacao(unittest.TestCase):

    def test_criacao_conta_com_sucesso(self):
        numero_conta = 1234
        agencia = 5432
        saldo_inicial = 1000

        conta = Conta(numero_conta, agencia, saldo_inicial)

        self.assertEqual(conta.numero, numero_conta)
        self.assertEqual(conta.agencia, agencia)
        self.assertEqual(conta.saldo, saldo_inicial)

    def test_criacao_conta_com_saldo_negativo(self):
        numero_conta = 1234
        agencia = 5432
        saldo_inicial = -100

        with self.assertRaises(ValueError):
            Conta(numero_conta, agencia, saldo_inicial)

class TestContaOperacoes(unittest.TestCase):

    def setUp(self):
        self.conta = Conta(1234, 5432, 1000)

    def test_deposito_com_sucesso(self):
        valor_deposito = 200

        self.conta.depositar(valor_deposito)

        self.assertEqual(self.conta.saldo, 1200)

    def test_deposito_com_valor_negativo(self):
        valor_deposito = -100

        with self.assertRaises(ValueError):
            self.conta.depositar(valor_deposito)

    def test_saque_com_sucesso(self):
        valor_saque = 500

        self.conta.sacar(valor_saque)

        self.assertEqual(self.conta.saldo, 500)

    def test_saque_com_valor_negativo(self):
        valor_saque = -100

        with self.assertRaises(ValueError):
            self.conta.sacar(valor_saque)

    def test_saque_com_saldo_insuficiente(self):
        valor_saque = 1500

        with self.assertRaises(SaldoInsuficienteException):
            self.conta.sacar(valor_saque)

class TestContaSaldoNegativo(unittest.TestCase):

    def test_criacao_conta_com_saldo_negativo(self):
        numero_conta = 1234
        agencia = 5432
        saldo_inicial = -100

        with self.assertRaises(ValueError):
            Conta(numero_conta, agencia, saldo_inicial)

    def test_saque_que_deixa_saldo_negativo(self):
        valor_inicial = 1000
        valor_saque = 1200  # Aumentado para garantir saldo negativo
        saldo_esperado = -200

        conta = Conta(1234, 5432, valor_inicial)
        conta.sacar(valor_saque)

        self.assertEqual(conta.saldo, saldo_esperado)
