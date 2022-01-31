from src.Figure import Figure
from math import pi
class Circle(Figure):
    def __init__(self,r):
        self.name = "Circle"
        self.r = r
        self.perimetr=2*pi*self.r
        self.area=pi*self.r*self.r


#ex1=Circle(10)
#print(ex1.perimetr)
#print(ex1.area)
#print(ex1.add_area(Triangle(3,4,5)))

