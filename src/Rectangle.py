from src.Figure import Figure
class Rectangle(Figure):
    def __init__(self,a,b):
        self.name = "Rectangle"
        self.a = a
        self.b = b
    def get_perimetr(self):
            return 2*(self.a + self.b)
    def get_area(self):
            return self.a * self.b

