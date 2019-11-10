def cadastro(codigo, produto, quantidade, preco):
    f = open('txt/mercado1.txt', 'a')
    total = quantidade*preco
    f.write('%d|'%codigo + '%s|'%produto + '%.2f\n'%total)
    f.close()

def ler_dados():
    quantidade_lista_compras = int(input("Quantidade na lista: "))
    
    for x in range(quantidade_lista_compras):
        tipo_mercado = int(input("Tipo do mercado: "))
        codigo = int(input("Codigo: "))
        produto = str(input("Produto: "))
        preco = float(input("Preço: "))
        quantidade_de_produto = int(input("Quantidade: "))
        preco_total = preco*quantidade_de_produto

        cadastro(codigo, produto, quantidade_de_produto, preco)

init_progam = ler_dados()
