#multiplas entradas na mesma linha de um input

dados = input('digite o seu nome, idade e estado:').split()
nome = dados[0]
idade = dados[1]
estado = dados[2]

print(f"""Olá {nome.upper()}!
Você tem {idade} anos e
Mora no estado de {estado.upper()}!""")