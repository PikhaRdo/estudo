#polimorfismo

class Personagens():
    def falar(self):
        print("teste")

class Guerreiro(Personagens):
    def falar(self):
        print("eu sou um guerreiro")
class Mago(Personagens):
    def falar(self):
        print("Sou um mago de fogo")

class Arqueiro(Personagens):
    def falar(self):
        print("Minha mira é precisa")


#Criação dos objetos
#lista de objetos
personagens = [Guerreiro(), Mago(), Arqueiro()]
