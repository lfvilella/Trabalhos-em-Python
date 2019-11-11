import csv

def limpar_file_before_start():
    for arquivo in range(1,4):
        file_name = 'txt/mercado{}.txt'.format(arquivo)
        open(file_name,'w').close()

def cadastro(codigo, produto, quantidade, preco, tipo_do_mercado):
    total = preco*quantidade

    file_name = 'txt/mercado{}.txt'.format(tipo_do_mercado)

    with open(file_name, 'a', newline='') as csvfile:
        fieldnames = ['product', 'total_cost']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'product': produto, 'total_cost': total})

def compara_precos():
    produto_valor = {}
    todos_produtos = set()
    for mercado in range(1, 4):
        file_name = 'txt/mercado{}.txt'.format(mercado)

        with open(file_name) as csvfile:
            fieldnames = ['product', 'total_cost']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)

            for row in reader:
                # coloca todos os produtos em uma lista unica
                todos_produtos.add(row['product'])

                # agrupar os precos por produto e mercado {'carvao': {<mercado>: <valor>, 2: 5.5, 3: 15}}
                if row['product'] not in produto_valor:
                    produto_valor[row['product']] = {}
                produto_valor[row['product']][mercado] = float(row['total_cost'])

    total_por_mercado = {1: 0.0, 2: 0.0, 3: 0.0}
    produtos_ordenados_por_nome = sorted(list(todos_produtos))

    for produto in produtos_ordenados_por_nome:
        valores_por_mercado = produto_valor[produto]

        # se não tiver preço para os 3 mercados ignorar produto
        if len(valores_por_mercado) != 3:
            continue

        for mercado, valor in valores_por_mercado.items():
            total_por_mercado[mercado] += valor

    return total_por_mercado

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

        cadastro(codigo, produto, quantidade_de_produto, preco, tipo_mercado)

if __name__ == '__main__':
    limpar_file_before_start()
    init_progam = ler_dados()

    precos_mercados = compara_precos()
    for mercado, precos in precos_mercados.items():
        print("Mercado", mercado, "total =", precos)