class Cylinder(object):
    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.radius ** 2 * self.height * self.pi
    
    def surface_area(self):
        return self.radius ** 2 * self.pi

c = Cylinder(2,2)

print(c.volume())
print(c.surface_area())