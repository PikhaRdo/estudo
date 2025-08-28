#input do usuario
idade = int(input("digite sua idade: "))


#condicionais para verificar se o usuario é maior de idade, se for verdadeiro
if idade >= 18:
    print(f"""Você tem {idade} anos
Você é considerado um adulto""")
#condicionais para verificar se o usuario é um adolescente
elif idade<18 and idade>=14:
    print(f"""Você tem {idade} anos
Você é considerado um adolescente""")

#se for falso:
else:
    print(f"""Você tem {idade} anos, 
Você ainda é uma criança""")