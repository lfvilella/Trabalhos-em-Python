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
    for codigo_mercado in range(1,4):
        valor = pesquisa_valor(codigo_mercado, produto)
        if valor:
            lista.append({'valor': valor, 'mercado':codigo_mercado}) # codigo_mercado = Se é o mercado 1,2 ou 3.

    lista.sort(key=lambda obj: obj['valor'])

    if not lista:
        return 
    
    return lista[0]

def produtos_mercados_ordenados():
    produtos = []
    for mercado in range(1,4):
        file_name = 'txt/mercado{}.txt'.format(mercado)
        
        with open(file_name) as csvfile:
            fieldnames = ['product', 'total_cost']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)

            for row in reader:
                if not mercado_mais_barato(row['product']) in produtos:
                    produtos.append(mercado_mais_barato(row['product']))

    produtos.sort(key=lambda obj: obj['valor'])
    return produtos

def retorna_produto_e_preco(produto):
    lista = []
    valor_inexistente = 0
    for codigo_mercado in range(1,4):
        valor = pesquisa_valor(codigo_mercado, produto)
        if valor:
            lista.append({'valor': valor, 'mercado':codigo_mercado})
        else: 
            valor_inexistente += 1

    lista.sort(key=lambda obj: obj['valor'])

    if not lista:
        return

    if valor_inexistente > 0:
        return

    return lista

def calcula_diferenca(produto):
    lista = retorna_produto_e_preco(produto)
    diferenca = []
    valor_mais_barato = lista[0]
    for dicionario in lista:
        calculo_da_diferenca = dicionario['valor'] - valor_mais_barato['valor']
        mercado = dicionario['mercado']
        diferenca.append({'diferença': calculo_da_diferenca, 'mercado': mercado})

    del(diferenca[0]) # Tira a comparação do proprio mercado
    return diferenca

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
    lista_produtos = []
    quantidade_lista_compras = int(input("Quantidade na lista: "))
    
    for x in range(quantidade_lista_compras):
        tipo_mercado = int(ler_input("Tipo do Mercado: "))
        codigo = int(ler_input("Codigo: "))
        produto = str(ler_input("Produto: "))
        preco = float(ler_input("Preço: "))
        quantidade_de_produto = int(ler_input("Quantidade: "))
        lista_produtos.append(produto)

        cadastro(codigo, produto, quantidade_de_produto, preco, tipo_mercado)

if __name__ == '__main__':
    init_progam = ler_dados()
    # print(mercado_mais_barato('laranja'))
    # print(produtos_mercados_ordenados())
    # variavel_mercado_barato = total_compra_cheaper_supermarket()[1]
    # variavel_valor_mercado_barato = total_compra_cheaper_supermarket()[0]
    # print("O mercado", variavel_mercado_barato, "é o mais barato, seu total é =", variavel_valor_mercado_barato)
    # print(calcula_diferenca('laranja'))
    # print(retorna_produto_e_preco('laranja'))
    print(compara_precos())