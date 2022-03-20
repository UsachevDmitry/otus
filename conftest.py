import pytest
import requests
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

@pytest.fixture
def service_1_url():
    service_1 = 'https://dog.ceo/api/breed'
    yield service_1

@pytest.fixture
def service_2_url():
    service_2 = 'https://api.openbrewerydb.org/breweries'
    yield service_2

@pytest.fixture
def service_3_url():
    service_3 = 'https://jsonplaceholder.typicode.com/'
    yield service_3

def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru")
    parser.addoption("--status_code", default="200")

@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")