lista = []

class Cidade:
    def __init__(self, consumo, moradores):
        self.consumo = consumo
        self.moradores = moradores

    def __repr__(self):
        return '%s-%s' % (self.moradores, self.consumo)

    def __lt__(self, c):
        if self.consumo == c.consumo:
            return self.moradores + c.moradores

    
if __name__ == '__main__':
    media_consumo = 0
    contador_moradores = 0
    cidade = 1 # Para printar no Cidade#

    quantidade_imoveis = int(input())
    while True:
        if quantidade_imoveis == 0:
            break

        else:
            for i in range(quantidade_imoveis):
                moradores, consumo = list(map(int, input().split()))
                contador_moradores += moradores
                media_consumo += consumo
                consumo = (consumo/moradores)
                values = Cidade(consumo, moradores)
                lista.append(values)
            # lista.sort()

            media_consumo = (media_consumo/contador_moradores)
            print("Cidade# %d:" % cidade)
            for i in lista:
                print(i)
            print("Consumo medio:", media_consumo)
            media_consumo = 0
            contador_moradores = 0
            cidade += 1

            quantidade_imoveis = int(input())
            if quantidade_imoveis != 0:
                print()
            lista.clear()



