import csv

def cadastro(codigo, produto, quantidade, preco, tipo_do_mercado):
    total = quantidade*preco

    file_name = 'txt/mercado{}.txt'.format(tipo_do_mercado)

    with open(file_name, 'a', newline='') as csvfile:
        fieldnames = ['product', 'total_cost']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'product': produto, 'total_cost': total})

def ler_dados():
    quantidade_lista_compras = int(input("Quantidade na lista: "))
    
    for x in range(quantidade_lista_compras):
        tipo_mercado = int(input("Tipo do mercado: "))
        codigo = int(input("Codigo: "))
        produto = str(input("Produto: ")).lower()
        preco = float(input("Preço: "))
        quantidade_de_produto = int(input("Quantidade: "))
        preco_total = preco*quantidade_de_produto

        cadastro(codigo, produto, quantidade_de_produto, preco, tipo_mercado)

# def mercado_mais_barato():


init_progam = ler_dados()
