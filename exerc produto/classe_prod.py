class Produto:
    def __init__(self,nome, preco):
        self.nome=nome
        self.preco=preco

    def aplicar_desconto(self, desconto):
        self.preco =self.preco - (self.preco * (desconto/100))
        return self.preco
    
    def exibir_produto (self):
        print (f"O produto é {self.nome} e seu valor com desconto é de {self.preco.2f}")

