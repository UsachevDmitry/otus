from math import sqrt
from src.Figure import Figure
class Triangle(Figure):
    # Проверка условия возможности данного Треугольника
    def __new__(cls, a, b, c):
        if (a > (b + c) or
             a < (b - c) or
             b > (a + c) or
             b < (a - c) or
             c > (a + b) or
             c < (a - b) or
             a==0 or b==0 or c==0):
            return None
        else:
            return super().__new__(cls)
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.name = "Triangle"
        self.perimetr = (self.a + self.b + self.c)
        p = (self.a + self.b + self.c) / 2
        self.area = (sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)))




#ex2=Triangle(4,5,6)
#print(ex2.perimetr)
#print(ex2.area)
#print(ex2.name)

