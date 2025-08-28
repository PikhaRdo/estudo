#Sistema de desconto
#Compra de qualquer valor = 5%
#compras acima de R$100 = 10%
#compras acima de R$200 = 20%
#Usuario tem que entrar com o valor da compra

valor = float(input("Digite o valor do produto: "))

if valor>=100 and valor<200 :
    desc = valor * 0.90
    print(f"""Desconto de 10%
    valor = {desc}""")

elif valor>=200:
    desc = valor * 0.80
    print(f"""Desconto de 20%
    Valor Final = {desc}""")

else:
    desc = valor * 0.95
    print(f"""desconto de 5%
Valor Final = {desc}""")