#Classes

class Livros:
    def __init__(self, titulo, autor , disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = bool(disponivel)


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adic_livros(self):
        self.livros.append(livro)

    def listagem_livros(self):
        for livro in self.livros:
            print(f"""Autor = {livro.autor}
Titulo = {livro.titulo}
Disponibilidade = {livro.disponivel}""")


livro = Livros('pequeno principe', 'N/A', False)


biblioteca = Biblioteca()
biblioteca.adic_livros()
biblioteca.listagem_livros()
