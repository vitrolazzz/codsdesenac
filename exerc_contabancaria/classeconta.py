class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular=titular
        self.saldo=saldo
    def depositar(self,valor):
        self.saldo=self.saldo+valor
        print(f"Agora o valor de {self.titular} é {self.saldo}")
    def sacar(self,valor2):
        if valor2 <0:
            print ("O valor não pode ser menor que 0")
        elif(self.saldo-valor2<=0):
            print ("Seu saldo é insuficiente!")
        else:
            self.saldo = self.saldo-valor2
            print (f"Agora o saldo de {self.titular} é {self.saldo}") 
    def consultar_saldo(self):
        print(f"O saldo de {self.titular} é de {self.saldo}")