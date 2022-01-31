from src.Figure import Figure
#from math import pi
from src.Circle import Circle
class Rectangle(Figure):
    def __init__(self,a,b):
        self.name = "Rectangle"
        self.a = a
        self.b = b
        self.perimetr = 2*(self.a + self.b)
        self.area = self.a * self.b



