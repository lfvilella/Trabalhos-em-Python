# Longe de estar completo

def employees(funcionarios):
    salario_minimo = 998
    gasto_com_funcionario = funcionarios*salario_minimo
    return gasto_com_funcionario

def warehouse(produto, quantidade,x,y):
    valor_dos_produtos = float(input("Insira o preço do produto %s: "%produto))
    preco_produto = valor_dos_produtos*quantidade
    return preco_produto


print("Bem vindo a Simplified Corporation !")
access = 1
print(" ")
print("Para administrar os funcionários, digite 1")
print("Para administrar o estoque, digite 2")
print("Para administrar as vendas, digite 3")
print("Para administrar as contabilidades, digite 4")
print(" ")
print("Press 0 for quit")

while access != 0:
    access = int(input("Enter a pass: "))

    # Funcionarios
    if access == 1:
        funcionarios = int(input("Insira a quantidade de funcionarios na empresa: "))
        print("Seu gasto com %d"%funcionarios,"funcionarios é %.2f"%employees(funcionarios))

    # Estoque
    elif access == 2:
        nome_produto = str(input("Nome do produto: "))
        quantidade_produto = int(input("Quantidade do produto %s "%nome_produto))
        print("Seu estoque é de %d"%quantidade_produto, "%s."%nome_produto, "Valendo = %.2f"%warehouse(nome_produto,quantidade_produto))
        
    # Vendas
    elif access == 3:
        produto_vendido = str(input("Produto a ser vendido: "))
        quantidade_produto = int(input("Quantidade do produto %s a ser vendido: "%produto_vendido))
    # Contabilidade
    elif access == 4:
        print("Press 0 for quit")

    elif access == 0:
        break

    else:
        print("Invalid Type !")

# print(employees(funcionarios))
# print(warehouse(estoque))