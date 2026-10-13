class ContaBancaria:
    def __init__ (self, saldo_travado):
        self.__travado=saldo_travado
    def depositar (self, valor):
        if valor>0:
            self.__travado += valor
    def get_saldo(self):
        return self.__travado
    
conta = ContaBancaria (1000)
conta.depositar (500)
print(conta.get_saldo())
