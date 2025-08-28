#Sistema de Universidade

class Universidade():
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade= idade
        self.status= status
    def apresentacao(self):
        print(f"Meu nome é {self.nome}")
    def verificar_status(Self,status):
        if status:
            print("O contrato está ativo para essa pessoa")
        else:
            print("Contrato Inativo!")
        


class Aluno(Universidade):
    def __init__(self,nome, idade, curso,status):
        super().__init__(nome,idade, status)
        self.curso= curso
    def apresentacao(self):
        super().apresentacao()
        print("Aluno")
    def verificar_status(Self, status):
        return super().verificar_status(status)



class Professor(Universidade):
    def __init__(self,nome,idade,materia,status):
        super().__init__(nome,idade,status)
        self.materia=materia
    def apresentacao(self):
        super().apresentacao()
        print("Professor")

class Assistente(Universidade):
    def __init__(self,nome,idade,bloco,status):
        super().__init__(nome,idade,status)
        self.bloco=bloco
    def apresentacao(self):
        super().apresentacao()

    

a1 = Aluno("Ricardo", 20, "Segurança da Informação", True)
p1 = Professor("Eduardo", 45, "Gestão", False)
""" as1= Assistente("ana", 25,"Bloco 3", True ) """


print(p1.nome , p1.idade, p1.materia)
a1.verificar_status()


