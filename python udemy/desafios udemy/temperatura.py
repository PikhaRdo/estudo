#desafio: crie um programa que controle a temperatura,
# aonde nesse controle: se for menor doq 15C é pra retornar que esta muito frio,
#menor doq 25c = fresco
#restante = esta quente

temp = float(input("digite a temperatura atual: "))

if temp<=15:
    print(f"""Temperatura atual de {temp:.2f}, está muito frio!!!!
Recomenda-se roupas mais grossas""")

elif temp>15 and temp<=25:
    print(f"""Temperatura atual de {temp:.2f}, o tempo está fresco
Recomenda-se roupas mais leves""")

else:
    print(f"""Temperatura atual de {temp:.2f}, está fazendo calor!!!
recomenda-se roupas mais curtas e beba bastante água!""")