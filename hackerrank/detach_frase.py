def separate_string(frase):
    return print(''.join(frase[::2]), ''.join(frase[1::2]))

if __name__ == '__main__':
    t = 0
    while t < 1 or t > 10:
        t = int(input())
    
    for idx in range(t):
        lenght = 1
        frase = ''
        while lenght < 2 or lenght > 10000:
            frase = str(input())
            lenght = len(frase)
        
        separate_string(frase)
