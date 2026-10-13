from veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, marca,portas):
        super().__init__(marca)
        self.portas=portas
    def ligar(self):
        print (f"Carro {self.marca} ligado")

        
