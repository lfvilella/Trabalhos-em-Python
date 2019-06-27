import unicodedata

quantidade_palavra = int(input())

cont = 0
while cont < quantidade_palavra:
    palavra = str(input()).lower()

    word_formatted = (
        unicodedata.normalize('NFKD', (palavra.replace(' ', '').lower()))
        .encode('ascii', 'ignore')
    )

    palavra_invertida = word_formatted[::-1]
    if word_formatted == palavra_invertida:
        print("SIM")
    else:
        print("NAO")        

    cont += 1
