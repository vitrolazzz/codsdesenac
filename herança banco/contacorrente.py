from conta import ContaBancaria
class ContaCor(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite=limite

    def exibir_dados(self):
        self.saldo = self.saldo + self.limite
        return self.saldo
    