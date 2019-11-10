# def cadastro()

def ler_dados():
    quantidade_lista_compras = int(input("Quantidade na lista: "))
    # f = open('txt/mercado1.txt', 'a')

    for x in range(quantidade_lista_compras):
        tipo_mercado = int(input("Tipo do mercado: "))
        codigo = int(input("Codigo: "))
        produto = str(input("Produto: "))
        preco = float(input("Preço: "))
        quantidade_de_produto = int(input("Quantidade: "))
        preco_total = preco*quantidade_de_produto

        # f.write(codigo + '|' + produto + '|' + preco_total)
        # cadastro(tipo_mercado, codigo, produto, preco_total)
    # f.close()

init_progam = ler_dados()