#o vendedor vai inserir o produto, em R$ e com um taxa de 10%
produto = str(input('Nome do produto: ')) #recebe o nome do produto
preco_orig = float(input("Preço do produto em R$: ")) #recebe o valor original do produto
preco_fin = float(preco_orig * 1.10) #calcula o valor do produto com os 10% de tarifa


print(f"""Produto adicionado: {produto}
Preço com a tarifa de 10%: R${preco_fin:.2f}""")