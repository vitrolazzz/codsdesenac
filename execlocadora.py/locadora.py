class Locadora:
    def __init__ (self):
        self.veiculos=[]
        self.clientes=[]
    def cadastrar_veiculo(self,veiculo):
        self.veiculos.append(veiculo)

    def cadastrar_cliente(self,cliente):
        self.clientes.append(cliente)

    def alugar_veiculo(self,cliente,veiculo,dias):
        if veiculo.disponivel == True:
            veiculo.disponivel = False

            valor=veiculo.valor_diaria*dias

            cliente.historico.append(f"{veiculo.modelo} - {dias} dias - R$ {valor}")

            print("Locação realizada!") 
            print("Valor total: R$", valor)

        else:
            print ("Veículo não está disponível")

    def devolver_veiculo(self, veiculo): 
        veiculo.disponivel = True 
        print("Veículo devolvido!")
    
