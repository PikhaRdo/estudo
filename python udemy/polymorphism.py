""" #polimorfismo

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
        print("Eu sou um arqueiro")


#Criação dos objetos
#lista de objetos
personagens = [Guerreiro(), Mago(), Arqueiro()]

#print todas as classes
for p in personagens:
    p.falar()

 """


""" #polymorphism sem herança

class Cachorro:
    def emitir_som(self):
        print('Latir')

class Gato:
    def emitir_som(self):
        print('Miar')

#lista de objetos
animais = [Cachorro(), Gato()]
for animal in animais:
    animal.emitir_som()
 """