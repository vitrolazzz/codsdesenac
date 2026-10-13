class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    def apresentar (self):
        return f"Olá, sou {self.nome}"

p1 = Pessoa("Ana",25)
print(p1.apresentar())

p2 = Pessoa("José",29)
p3 = Pessoa("João",30)
p4 = Pessoa("Maria",19)

print(p2.apresentar())
print(p3.apresentar())
print(p4.apresentar())