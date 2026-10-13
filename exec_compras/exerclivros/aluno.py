class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def adicionar_livro(self, livro):
        self.livros_emprestados.append(livro)

    def remover_livro(self, livro):
        self.livros_emprestados.remove(livro)

    def listar_livros(self):
        print(f"\nLivros de {self.nome}:")

        if len(self.livros_emprestados) == 0:
            print("Nenhum livro emprestado.")
        else:
            for livro in self.livros_emprestados:
                print(f"- {livro.titulo}")