from conta import ContaBancaria
from contacorrente import ContaCor
from contapou import ContaPou

c1 = ContaCor("Maria",10,100)
c2=ContaPou("José",12,1)
print(c1.exibir_dados())
print(c2.render_juros())
