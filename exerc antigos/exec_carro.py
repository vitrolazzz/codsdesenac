class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def exibir_dados(self):
        print (f"Esse modelo é um {self.modelo} da {self.marca} produzido no ano {self.ano}")



