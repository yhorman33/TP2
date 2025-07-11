class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial=0.0):
        self.__numeroCuenta = numero_cuenta
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito: ${cantidad:.2f}")
        else:
            print("Monto inválido.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro: ${cantidad:.2f}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def getSaldo(self):
        return self.__saldo
