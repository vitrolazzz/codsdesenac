class Biblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)
        print("Livro cadastrado com sucesso!")

    def listar_livros(self):
        print("\n--- LIVROS DA BIBLIOTECA ---")

        if len(self.livros) == 0:
            print("Nenhum livro cadastrado.")
        else:
            for livro in self.livros:
                print(livro)

    def emprestar_livro(self, livro, aluno):

        if livro.disponivel:
            livro.disponivel = False
            aluno.adicionar_livro(livro)

            print(
                f"\nLivro '{livro.titulo}' emprestado "
                f"para {aluno.nome}."
            )
        else:
            print(f"\nO livro '{livro.titulo}' já está emprestado.")

    def devolver_livro(self, livro, aluno):

        if livro in aluno.livros_emprestados:
            livro.disponivel = True
            aluno.remover_livro(livro)

            print(
                f"\nLivro '{livro.titulo}' devolvido "
                f"por {aluno.nome}."
            )
        else:
            print(
                f"\n{aluno.nome} não possui "
                f"o livro '{livro.titulo}'."
            )
