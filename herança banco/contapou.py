from conta import ContaBancaria
from contacorrente import ContaCor

class ContaPou(ContaBancaria):
    def __init__(self,titular,saldo,taxa_juros):
        super().__init__(titular,saldo)
        self.taxa_juros=taxa_juros

    def render_juros(self):
        self.saldo=self.saldo+(self.saldo*self.taxa_juros)
        return self.saldo
    