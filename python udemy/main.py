#o código principal vai ficar aqui
# from func import saudacao , soma , maior
#
# nome = str(input("""Qual o seu nome uwu? """))
# idade= int(input("""Quantos anos você tem?
# """))
#
# saudacao(nome)
# # print(soma(a = int(input("Valor de a:")), b= int(input("Valor de b:") )))
# if maior(idade):
#     print(f"Você já é bem grandinha owo")
# else:
#     print(f"Saia cria de baphomé ")



#mais de oop
#atributos: cor, ano, marca, modelo
class Carro:
    def __init__(self, cor, ano, marca, modelo):
        self.cor = cor
        self.ano = ano
        self.marca = marca
        self.modelo = modelo
        self.ligado =True
        self.seta = None
    def inf(self):
        print(f"""O carro é {self.cor},
Ano de fabricação: {self.ano},
Marca: {self.marca}
Modelo: {self.modelo}""")
    def ligar(self):
        if not self.ligado:#se não for verdadeiro
            self.ligado = True
            print("Ligando carro...")
        else:
            print("O carro já estava ligado")
    def desligar(self):
        if self.ligado==True:
            self.ligado = False
            print("O carro foi desligado")
        else:
            print("O carro já estava desligado")
    def ligar_seta(self,direcao):
        if self.ligado:
            self.seta = direcao
            print(f'Seta ligada para a {self.seta}')
        else:
            print("O carro está desligado, não é possivel ligar a seta!")


carro1 = Carro('Prata', 2015, "Honda", "Civic")
#parametros adicionais
carro1.inf(), carro1.ligar(), carro1.ligar_seta("direita")