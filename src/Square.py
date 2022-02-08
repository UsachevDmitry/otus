from src.Rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, a):
        self.name = "Square"
        self.a = a
    def get_perimetr(self):
        return 2 * (self.a + self.a)
    def get_area(self):
        return self.a * self.a
