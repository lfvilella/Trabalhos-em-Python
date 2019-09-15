def maior(a,b,c):
    # abs retorna o valor absoluto, o modulo das variaveis
    maior_ab = (a+b+(abs(a-b)))/2
    maior_de_todos = (maior_ab+c+(abs(maior_ab-c)))/2

    return maior_de_todos

num1 = int(input())
num2 = int(input())
num3 = int(input())

# para nao printar float
print("%d eh o maior"%maior(num1,num2,num3))