lista_camisas = []
class Camiseta:
	def __init__(self, name, cor, tam):
		self.name = name
		self.cor = cor
		self.tam = tam

	def __repr__(self):
		return '%s %s %s' % (self.cor, self.tam, self.name)

	def __lt__(self, c):
		if self.cor != c.cor:
			return self.cor < c.cor
		elif self.tam != c.tam:
			return self.tam > c.tam
		else:
			return self.name < c.name

if __name__ == '__main__':
    n = int(input())
    while True:
        if n == 0:
            break
        else:
            for i in range(n):
                name = str(input())
                cor, tam = list(map(str, input().split()))
                values = Camiseta(name, cor, tam)
                lista_camisas.append(values)
            lista_camisas.sort()

            for i in lista_camisas:
                print(i)

            n = int(input())
            if n != 0:
                print()
            lista_camisas.clear()