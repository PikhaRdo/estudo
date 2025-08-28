# #financ
#
# renda = False
# nome_l = False
#
# if renda or nome_l:
#     print("financiamento aprovado")
#
# else:
#     print("financiamento reprovado")


#
# prod = str(input("digite o nome do produto: "))
# valor = float(input("digite o valor do produto: "))
#
# if 40>valor>=20:
#     print(f"""Novo produto adicionado = {prod}
# Valor = {valor}""")
# else:
#     print("produto não aceito por valor invalido.")
#
# ------------------------------FOR----------------------------

#imprimir de 1 a 5
# x = 0
# for x in range(0, 10, 1):
#     print(x)
#     print("+ 1")
#     if x == 5:
#         print(x)
#         break
#     elif x>5:
#         print(f"{x} passou de 5")
#         break
#     else:
#         print("erro")
#

#for para strings
#palavra = "gooooooooogle"
#
# for letra in palavra:
#    print( letra + " esta dentro da palavra google")

#for loop com if e else

# compra_conf = True
# dados_compra = "Compra no valor de RS12.50 e entrega confirmada."
# #laço aonde é testado 3 vezes a condicional de compra,
# #sendo ela verdadeira ela executa normalmente, sendo ela errada ou falsa
# #ela vai pro else e quebra.
#
# for enviar in range(3):
#     if compra_conf:
#         print(f'{dados_compra}')
#         print("Detalhes enviados para o seu email.")
#         break
# else:
#     print("Falha na compra")

#
# for numero in range(5):
#     print(str(numero) + " +1 laço")
#     for numero1 in range(5):
#         print(numero1, numero)


#for loop - separando strings
# palavra = "FANTASTICO"
# for espaco in palavra:
#     print(espaco, end=' ')


#for loop criando um retangulo
#
# linhas = 6
# colunas = 6
# simbolo = "-"
#
# for l in range(linhas):
#     print( ) #quebra de linha
#     for c in range(colunas):
#         print(simbolo , end="")


# #while loop
# valor = 100
# dia = 0
# while valor>20:
#     dia += 1
#     print(f"No {dia}°, o valor do produto é de R${valor}")
#     print()
#     valor -= 5
#
# #ternary operator
# idade = int(18)
# resultado = "Voto permitido" if idade>=16 else "Voto não permitido"
# print(resultado)

# valor = float(input("Digite o valor do Produto: "))
#
# while valor>=20:
#     valor = valor * 1.1
#     print(f"O valor final do Produto será de R${valor} ")
#     break
# else:
#     print(f"O valor final será: {valor}")
#
# #lista, com laço de repetição para printar cada index
# frutas = ['Maçã',"abacate",'banana','limão','laranja','morango']
# num =int(0)
# #
# # frutas.append(input("adicione uma fruta: "))
# # frutas.remove('banana')
# while num<len(frutas):
#     print(frutas[num])
#     num+=1


tarefas = []
while True:
    opt= int(input('''Deseja adicionar uma tarefa?
    1 = Sim!
    2 = Não!
    R: '''))
    while opt == 1:
        tarefas.append(input("Que tarefa você vai realizar hoje?"))
        print(f"""Tarefa adicionada!
Tarefas: {tarefas}""")
        opt = int(input("""Deseja Adicionar mais tarefas?
            1 = Sim!
            2 = Não!
            R: """))
        if opt==0:
            print(f"""Tarefas atuais: {tarefas}.
fechando o programa.""")
            break
    if opt ==2:
        print(f"""Tarefas atuais: {tarefas}.
Fechando o programa.""")
        break
    else:
        print("Opção invalida!")


#tuplas

#criando tuples
#
# meses =('janeiro','fevereiro','março')
# print(meses[0])
#
#dicionarios
# usuario = {
#     'Nome': 'Ricardo',
#     'idade': 20,
#     'departamento': 'TI'
# }
# usuario['idade']=  30
# usuario['cidade']= 'ourinhos'
# print(usuario)
#dicionario de um aluno
# aluno ={
#     'Nome': input('nome do aluno: '),
#     'Idade': int(input('idade do aluno:')),
#     'Curso':input('Curso do aluno: ')
# }
#
# print(f"""O aluno se chama: {aluno['Nome']}.
# Tem {aluno['Idade']} anos e
# Está cursando {aluno['Curso']}.""")

    #tarefas.append(str(input('Quais tarefas você vai realizar hoje?')))




#funções reutilizaveis

# def saudacoes(nome, idade):
#     print(f'Olá {nome}, {idade}!!!')
#     print(type(idade))
#
# saudacoes('Ricardo', 20)
# saudacoes('ana', 20)
#
# def somar(nu1,nu2):
#     nu1 = float(input("Digite o 1° valor:"))
#     nu2 = float(input("Digite o 2° valor:"))
#
#     return nu1 + nu2
#
#
# total = somar(20, 20)
# print(f"O resultado da soma é de {total}")

# def desconto(preco,porcentagem):
#     return preco - (preco* porcentagem/100)
#
# final = desconto(preco=float(input("Digite o preço: ")), porcentagem=float(input("Digite a porcentagem de desconto:")))
# print(f"O valor final é de R${final:.2f}")
# ###################3
# class Casa:
#     def __init__(self,cor, quartos, banheiros): #construtor
#         self.cor= cor
#         self.quartos = quartos
#         self.banheiros= banheiros
# #metodos
#     def mostrar_cor (self):
#         print(f"A cor da casa é {self.cor} \n")
#     def mostrar_quartos(self):
#         print(f"Está casa tem {self.quartos} quartos\n")
#     def mostrar_banheiros(self):
#         print(f"Está casa tem {self.banheiros} banheiros\n")
#     #adiciona + 1 quarto
#     def adicionar_quarto(self):
#         self.quartos +=1
#         print(f'Esta casa tem {self.quartos} quartos')
#     def troca_cor(self, nova_cor):
#         print(f'Esta casa era {self.cor} e agora é {nova_cor}')
#
# #instancias
# casa1 = Casa('Azul', 3, 1)
# casa2 = Casa('Amarela', 6, 3)
# #chamando os metodos
# print('\n\ncasa1:')#metodos
# casa1.mostrar_cor(), casa1.mostrar_quartos(), casa1.mostrar_banheiros(), casa1.adicionar_quarto()
# print('\n\ncasa2: ')#metodos
# casa2.mostrar_cor(), casa2.mostrar_quartos(), casa2.mostrar_banheiros(), casa2.troca_cor('verde')
#
#
#

#
# lang = str(input("Linguagem: "))
# def linguagem(lang):
#     while True:
#         match lang:
#             case "Java":
#                 print("Linguagem: Java")
#                 break
#             case "Python":
#                 print("Pythons")
#                 break
#             case _:
#                 print("Opção invalida, rode o programa novamente")
#                 break
#
#
#
# lang = "Python"
# linguagem(lang)