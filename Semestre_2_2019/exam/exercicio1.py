import csv

def cadastro(codigo, produto, quantidade, preco, tipo_do_mercado):
    total = quantidade*preco

    file_name = 'txt/mercado{}.txt'.format(tipo_do_mercado)

    with open(file_name, 'a', newline='') as csvfile:
        fieldnames = ['product', 'total_cost']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'product': produto, 'total_cost': total})

def pesquisa_valor(codigo_arquivo, produto):
    file_name = 'txt/mercado{}.txt'.format(codigo_arquivo)
    
    # soma_valor = 0 -> Caso haja uma repetição nos produtos, mas na lógica não deveria haver.
    with open(file_name) as csvfile:
        fieldnames = ['product', 'total_cost']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)

        for row in reader:
            if row['product'] == produto:
                return float(row['total_cost'])

    # return soma_valor

def mercado_mais_barato(produto):
    lista = []
    for idx in range(3):
        lista.append(pesquisa_valor(idx+1, produto))

    lista.remove(None)
    lista.sort()
    # print(lista)

def ler_input(msg=None):
     return input(msg).lower().strip()

def ler_dados():
    quantidade_lista_compras = int(input("Quantidade na lista: "))
    
    for x in range(quantidade_lista_compras):
        tipo_mercado = int(ler_input("Tipo do Mercado: "))
        codigo = int(ler_input("Codigo: "))
        produto = str(ler_input("Produto: "))
        preco = float(ler_input("Preço: "))
        quantidade_de_produto = int(ler_input("Quantidade: "))
        preco_total = preco*quantidade_de_produto

        cadastro(codigo, produto, quantidade_de_produto, preco, tipo_mercado)
    
# init_progam = ler_dados()
mercado_mais_barato('laranja')