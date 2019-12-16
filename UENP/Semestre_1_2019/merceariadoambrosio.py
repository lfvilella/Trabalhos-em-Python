produto = int(input("Insira o produto: "))
quantidade  = int(input("Insira a quantidade: "))
desconto = 0.15
p1 = 5.30
p2 = 6
p3 = 3.20
p4 = 2.50

if produto == 1:
    total = quantidade*p1
    if (total >= 15 or quantidade > 40):
        total = (quantidade*p1) - ((quantidade*p1)*desconto)
        print("Total é: ", total)

    else:
        print("Total no else:", total)

elif produto == 2:
    total = quantidade*p2
    if (total >= 15 or quantidade > 40):
        total = (quantidade*p2) - ((quantidade*p2)*desconto)
        print(total)

    else:
        print(total)

elif produto == 3:
    total = quantidade*p3
    if (total >= 15 or quantidade > 40):
        total = (quantidade*p3) - ((quantidade*p3)*desconto)
        print(total)

    else:
        print(total)

elif  produto == 4:
    total = quantidade*p4
    if (total >= 15 or quantidade > 40):
        total = (quantidade*p4) - ((quantidade*p4)*desconto)
        print(total)

    else:
        print(total)

else: 
    print("Invalido !")

