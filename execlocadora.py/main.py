from cliente import Cliente
from locadora import Locadora
from veiculo import Veiculo

locadora = Locadora()

carro1 = Veiculo("Vectra", "KYD8C88", 100)
carro2 = Veiculo("Civic", "FOL1R85", 150)

locadora.cadastrar_veiculo(carro1)
locadora.cadastrar_veiculo(carro2)

cliente1 = Cliente("Mario")

locadora.cadastrar_cliente(cliente1)

locadora.alugar_veiculo(cliente1, carro1, 5)

print("\nHistórico do cliente:")
print(cliente1.historico)

locadora.devolver_veiculo(carro1)

