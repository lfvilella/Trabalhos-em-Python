def media(lista):
    resultado = 0
    for x in lista:
        resultado += x
    return resultado/(len(lista))

if __name__ == "__main__":
    lista = []
    for num in range(4):
        nota = float(input("Digite a nota: "))
        lista.append(nota)
    
    print("A media das 4 notas são:", media(lista))