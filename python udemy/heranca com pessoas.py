class pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"O meu nome é {self.nome} e tenho {self.idade} anos")

class funcionario(pessoas):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def trabalho(self):
        print(f"{self.nome} trabalha no setor de {self.cargo}")


class cliente(pessoas):
    pass



f1 = funcionario('Ricardo', 20 , "ti")
f1.apresentar(), f1.trabalho()

















