from exec_classe2 import Pessoa
galera = Pessoa("Allan",22)

escolha = int(input("Escolhar a pessoa para ser apresentada (1-2)\n"))
if escolha == 1:
    print(galera.apresentar())
elif escolha == 2:
    print(galera.apresentar())
else:
        print("Número inválido")