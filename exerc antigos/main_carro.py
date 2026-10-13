from exec_carro import Carro

c1= Carro("Ferrari","Testarossa",1984)
c2= Carro("Mercedes", "300SL", 1954)
c3 = Carro("Porsche", "911", 1948)

escolha = int(input("Escolha um dos carros para ser apresentado (1-3)\n"))
if escolha == 1:
    c1.exibir_dados()
elif escolha == 2:
    c2.exibir_dados()
elif escolha == 3: 
    c3.exibir_dados()