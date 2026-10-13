from carrinho import Carrinho
from produto import Produto

arroz = Produto("Arroz",25)
feijao = Produto("Feijão", 8.5)

carrinho = Carrinho()

carrinho.adicionar(arroz)

carrinho.listar_produtos()
print(carrinho.calcular_total())