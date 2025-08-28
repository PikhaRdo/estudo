class animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f"eu sou o {self.especie} chamado {self.nome} e eu sou {self.cor}")


class gato(animal):
    def miar(self):
        print("miau")
    def arranhar(self):
        print("o gato esta arranhando")
class cachorro(animal):
    def emitir_som(self):
        print("au?")


gato1= gato("cocozento", "laranja" ,"car")
gato1.apresentar(), gato1.miar(), gato1.arranhar()
cachorro1 = cachorro("russo" , "preto" , "Pastor Alemão")
cachorro1.apresentar(), cachorro1.emitir_som()

















