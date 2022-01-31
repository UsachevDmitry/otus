from src.Rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, a):
        self.name = "Square"
        self.a = a
        self.b = a
        self.perimetr = 2 * (self.a + self.b)
        self.area = self.a * self.b
#ex4=Square(2)
#print(ex4.perimetr)
#print(ex4.area)
#print(ex4.name)