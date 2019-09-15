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
        

cidade = 1 # Para printar no Cidade#
quantidade_imoveis = int(input())
while True:
    if quantidade_imoveis == 0:
        break

    else:
        c = CidadeConsumo()
        for i in range(quantidade_imoveis):
            moradores, consumo = list(map(int, input().split()))
            c.adicionar_casa(moradores, consumo)
        

        print("Cidade# %d:" % cidade)
        print(sorted(c.media_por_pessoa.items(), key=lambda i: i[1]))
        print("Consumo medio: %.2f m3." % c.consumo_medio)
        cidade += 1

        quantidade_imoveis = int(input())
        if quantidade_imoveis != 0:
            print()