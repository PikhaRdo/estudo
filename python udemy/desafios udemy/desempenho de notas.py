#maior q 9 = excelente, A
#maior q 7 = bom trabalho, B
#maior q 5 = passou, C
#qlqr outra = reprovado


nota = float(input("Digite a nota do aluno: "))

if nota>=9 :
    print("Nota excelente, tirou A")

elif nota<9 and nota>=7:
    print('Bom trabalho, tirou B')
elif nota<7 and nota>=5:
    print('Quase reprovou, tirou C')

else:
    print("Você foi reprovado otario")