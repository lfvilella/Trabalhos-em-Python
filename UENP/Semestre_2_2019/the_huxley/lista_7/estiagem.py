import collections
import dataclasses


@dataclasses.dataclass
class CidadeConsumo:
    casas: list = dataclasses.field(default_factory=list)
    media_por_pessoa: collections.Counter = dataclasses.field(
        default_factory=collections.Counter,
    )
    total_pessoas: int = 0
    total_consumo: float = 0
    consumo_medio: float = 0

    def adicionar_casa(self, quantidade_de_pessoas, consumo_de_agua):
        self.casas.append((quantidade_de_pessoas, consumo_de_agua))

        self.total_pessoas += quantidade_de_pessoas
        self.total_consumo += consumo_de_agua
        self.consumo_medio = self.total_consumo / self.total_pessoas

        media = consumo_de_agua / quantidade_de_pessoas
        self.media_por_pessoa[int(media)] += quantidade_de_pessoas

def ler_dados():
    cidades = []
    while True:
        quantidade_imoveis = int(input())
        if quantidade_imoveis == 0:
            break

        c = CidadeConsumo()
        for _ in range(quantidade_imoveis):
            moradores, consumo = list(map(int, input().split()))
            c.adicionar_casa(moradores, consumo)

        cidades.append(c)
    
    return cidades

def exibir_dados(cidades):

    index = 1
    for cidade in cidades:
        print(f'Cidade#: {index}')
        string = ''
        for media_consumo, quantidade_pessoas in sorted(cidade.media_por_pessoa.items(), key=lambda i: i[0]):
            string += f'{quantidade_pessoas}-{media_consumo} '
        print(string)
        print('Consumo medio: %.2f m3.' % cidade.consumo_medio)
        print()
        index += 1

if __name__ == '__main__':
    cidades = ler_dados()
    exibir_dados(cidades)
