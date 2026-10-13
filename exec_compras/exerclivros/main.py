from livro import Livro
from aluno import Aluno
from biblioteca import Biblioteca

biblioteca=Biblioteca()

# Criando livros
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
livro3 = Livro("Harry Potter", "J. K. Rowling")

# Cadastrando livros
biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_livro(livro2)
biblioteca.cadastrar_livro(livro3)

# Criando alunos
aluno1 = Aluno("João")
aluno2 = Aluno("Maria")


biblioteca.listar_livros()

# Emprestando livros
biblioteca.emprestar_livro(livro1, aluno1)
biblioteca.emprestar_livro(livro2, aluno2)

# Tentando emprestar um livro que já está emprestado
biblioteca.emprestar_livro(livro1, aluno2)

# Listando novamente
biblioteca.listar_livros()

# Mostrando livros de cada aluno
aluno1.listar_livros()
aluno2.listar_livros()

# Devolvendo um livro
biblioteca.devolver_livro(livro1, aluno1)

# Listando novamente
biblioteca.listar_livros()

# Mostrando novamente os livros do aluno
aluno1.listar_livros()