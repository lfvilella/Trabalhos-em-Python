class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2) ** 0.5
    
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return float((y2-y1)/(x2-x1))

cor1 = (3,2)
cor2 = (8,10)
l = Line(cor1, cor2)

print(l.distance())
print(l.slope())