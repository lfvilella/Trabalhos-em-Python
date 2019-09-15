stop=False
lista_idades=[]
lista_nomes=[]
lista_num_poltrona=[]

while stop!=True:
    numero_da_passagem=int(input())
    if numero_da_passagem==-1:
        stop=True
        break

    data=input()
    de=input()
    para=input()
    horario=input()
    poltrona=int(input())
    idade=int(input())
    nome_do_passageiro=input()
    lista_idades.append(idade)
    lista_nomes.append(nome_do_passageiro)
    lista_num_poltrona.append(poltrona)

media_idade=(sum(lista_idades)/len(lista_idades))

i=0
lista_nome_print=[]

while i < len(lista_idades):
    if lista_idades[i]>media_idade and lista_num_poltrona[i]%2==0:
        nome_print=i
        lista_nome_print.append(nome_print)
    i+=1

for i in lista_nome_print:
    print(lista_nomes[i])
  
  