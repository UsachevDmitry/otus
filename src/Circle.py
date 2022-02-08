from src.Figure import Figure
from math import pi
class Circle(Figure):
    def __init__(self,r):
        self.name = "Circle"
        self.r = r
    def get_perimetr(self):
        return 2*pi*self.r
    def get_area(self):
        return pi*self.r*self.r


