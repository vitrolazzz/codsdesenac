class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def remover(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)

    def listar_produtos(self):
        for p in self.produtos:
            print(f"Produto: {p.nome} | Preço: R$ {p.preco:.2f}")
    
    def calcular_total(self):
        total = 0

        for p in self.produtos:
            total += p.preco

        return total