from exercheran import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome,cargo):
        super().__init__(nome)
        self.cargo=cargo
    def apresentar(self):
        print (f"Sou {self.nome}. Cargo {self.cargo}")

        