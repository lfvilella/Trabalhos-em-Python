a = str(input())
b = str(input())

def diminuir(str):
    max = 50
    if len(str) > max:
        return str[:max]
    else:
        return str

a1 = diminuir(a)
b1 = diminuir(b)

if a1 == b1:
    print("IGUAIS")

else:
    print("DIFERENTES")
