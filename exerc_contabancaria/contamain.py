from classeconta import ContaBancaria
conta1 = ContaBancaria("Cassio",10)
conta2 = ContaBancaria("Luciana", 0)
conta3 = ContaBancaria("Daniela",15)
conta4=ContaBancaria("Mario",5)

conta1.consultar_saldo()
conta2.sacar(-5)
conta3.depositar(50)
conta4.sacar(10)