from func import saudacao
saudacao("Ricardowo")
class Pessoa:
    def __init__(self,nome ,idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo= cargo

    def inf(self):
        print(f"""Nome: {self.nome}
Idade: {self.idade}
Cargo: {self.cargo}\n """)
    def alt_cargo(self, novo_cargo):
        self.cargo = novo_cargo
        print(f"{self.nome} foi promovido(a) para a nova função de {novo_cargo}")
    def alt_idade(self, nova_idade):
        if nova_idade>self.idade:
            print(f"Atualizando a idade de {self.nome} para {nova_idade}")
            self.idade = nova_idade
        else:
            print("Erro!")

colaborador1= Pessoa("Ricardo", 20 , "Analista de TI Junior" )
colaborador1.alt_cargo('Analista de TI Pleno'), colaborador1.alt_idade(21) , colaborador1.inf()


# colaborador2= Pessoa("Rebeca" , 20 , "Dev Junior")
# colaborador2.inf()