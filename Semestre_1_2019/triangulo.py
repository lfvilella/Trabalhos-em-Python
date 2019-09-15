class Triangulo(object):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

t = Triangulo(2,2)
print(t.area())