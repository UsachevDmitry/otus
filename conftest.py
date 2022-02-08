import pytest
from src.Circle import Circle
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square
@pytest.fixture
def figure_incorrect_obj():
    incorrect_fig = ['String',0,None,True,False,6.55]
    yield incorrect_fig

@pytest.fixture
def figure_obj_names():
    triangle = Triangle(1, 3, 3)
    circle = Circle(3)
    square = Square(5)
    rectangle = Rectangle(2, 4)
    fig_objs_names = [triangle.name,circle.name,rectangle.name,square.name]
    yield fig_objs_names

@pytest.fixture
def figure_obj():
    triangle = Triangle(1, 3, 3)
    circle = Circle(3)
    square = Square(5)
    rectangle = Rectangle(2, 4)
    fig_objs = [triangle,circle,rectangle,square]
    yield fig_objs