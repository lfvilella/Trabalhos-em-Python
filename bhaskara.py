class Delta(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def delta(self):
        return (self.b * self.b) -4 * self.a * self.c

    def xix(self):
        if self.delta() == 0:
            print("Nao tem raiz")
        else:
            r1 = (-self.b + (self.delta() * 0.5)) / (2 * self.a)
            r2 = (-self.b - (self.delta() * 0.5)) / (2 * self.a)
            
            return r1, r2
        
a = int(input("Coloque o valor de a:"))
b = int(input("Coloque o valor de b:"))
c = int(input("Coloque o valor de c:"))

d = Delta(a, b, c)

print("Delta =", d.delta())
print("Raizes =", d.xix())