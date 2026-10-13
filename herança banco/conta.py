class ContaBancaria:
    def __init__(self,titular, saldo):
        self.titular=titular
        self.saldo=saldo
    

    def exibir_saldo(self):
        print (f"O titular da conta é {self.titular} e o saldo é {self.saldo} ")
        