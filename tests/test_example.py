import pytest
from math import pi
from math import sqrt
from src.Circle import Circle
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square
#Треугольник должен задаваться тремя сторонами, если треугольник создать нельзя то класс должен вернуть None
#Проверка на невозможность создать некорректный треугольник
def test_create_triangle_wrong_sides():
    triangle1=Triangle(1,1,3)
    assert (triangle1==None)
#Проверка на возможность создать треугольник
def test_create_triangle():
    triangle1 = Triangle(1, 3, 3)
    assert isinstance(triangle1, Triangle)
#Каждая фигура должна иметь атрибут name - название фигуры
def test_attr_name (figure_obj):
    for fig in figure_obj:
        if hasattr(fig,"name"):
            continue
        else:
            assert False
    assert True
#Каждая фигура должна иметь метод get_area (вычисляемое!) - площадь
def test_attr_area (figure_obj):
    for fig in figure_obj:
        fig_methods=dir(fig)
        if "get_area" in fig_methods:
            continue
        else:
            assert False
    assert True
#Каждая фигура должна иметь метод get_perimeter (вычисляемое!) - периметр
def test_attr_perimetr (figure_obj):
    for fig in figure_obj:
        fig_methods=dir(fig)
        if "get_perimetr" in fig_methods:
            continue
        else:
            assert False
    assert True
#Все вычисляемые свойства должны вычисляться по формулам для соответствующих геометрических фигур
#Круг периметр (Параметризацию просто было интересно попробовать, смысловой нагрузки в тесте не несет)
@pytest.mark.parametrize('testradius',[1,2,3])
def test_circle_perimetr(testradius):
    perimetr=2*pi*testradius
    fig=Circle(testradius)
    assert fig.get_perimetr() == perimetr
#Прямоугольник периметр
def test_rectangle_perimetr():
    side_a=2
    side_b=3
    perimetr = 2*(side_a + side_b)
    fig=Rectangle(side_a,side_b)
    assert fig.get_perimetr() == perimetr
#Квадрат периметр
def test_squre_perimetr():
    side=2
    perimetr = 2 * (side + side)
    fig=Square(side)
    assert fig.get_perimetr() == perimetr
#Треугольник периметр
def test_triangle_perimetr():
    side_a=2
    side_b=3
    side_c=2
    perimetr = (side_a + side_b + side_c)
    fig=Triangle(side_a,side_b,side_c)
    assert fig.get_perimetr() == perimetr
#Круг плошадь
def test_circle_area():
    radius=6
    area=pi*radius*radius
    fig=Circle(radius)
    assert fig.get_area() == area
#Прямоугольник плошадь                       
def test_rectangle_area():
    side_a=2
    side_b=3
    area = side_a * side_b
    fig=Rectangle(side_a,side_b)
    assert fig.get_area() == area
#Квадрат плошадь
def test_squre_area():
    side=2
    perimetr = 2 * (side + side)
    fig=Square(side)
    assert fig.get_perimetr() == perimetr
#Треугольник плошадь
def test_triangle_area():
    side_a=2
    side_b=3
    side_c=2
    p = (side_a + side_b + side_c) / 2
    area = (sqrt(p * (p - side_a) * (p - side_b) * (p - side_c)))
    fig=Triangle(side_a,side_b,side_c)
    assert fig.get_area() == area
#Каждая фигура должна реализовать метод add_area(figure) который должен принимать другую геометрическую фигуру и возвращать сумму площадей этих фигур.
#Круг
def test_circle_add_area(figure_obj):
    fig=Circle(6)
    for f in figure_obj:
        if (fig.get_area() + f.get_area()) == fig.add_area(f):
            continue
        else:
            assert False
    assert True
#Прямоугольник
def test_rectangle_add_area(figure_obj):
    fig=Rectangle(2,4)
    for f in figure_obj:
        if (fig.get_area() + f.get_area()) == fig.add_area(f):
            continue
        else:
            assert False
    assert True
#Квадрат
def test_square_add_area(figure_obj):
    fig=Square(7)
    for f in figure_obj:
        if (fig.get_area() + f.get_area()) == fig.add_area(f):
            continue
        else:                                           
            assert False
    assert True
#Треугольник
def test_triangle_add_area(figure_obj):
    fig=Triangle(7,8,9)
    for f in figure_obj:
        if (fig.get_area() + f.get_area()) == fig.add_area(f):
            continue
        else:                                         
            assert False
    assert True
#Если передана не геометрическая фигура, то нужно выбрасывать ошибку (raise ValueError) и сообщать что передан неправильный класс.
#Некоректные объект переданный в add_area
#Круг
def test_exception_circle(figure_incorrect_obj):
    fig=Circle(6)
    for f in figure_incorrect_obj:
        with pytest.raises(NotImplementedError) as e:
            fig.add_area(f)
        if "Incorrect class figure" in str(e):
            continue
        else:
            assert False
    assert True
#Прямоугольник
def test_exception_rectangle(figure_incorrect_obj):
    fig=Rectangle(6,7)
    for f in figure_incorrect_obj:
        with pytest.raises(NotImplementedError) as e:
            fig.add_area(f)
        if "Incorrect class figure" in str(e):
            continue
        else:
            assert False                             
    assert True
#Квадрат
def test_exception_squre(figure_incorrect_obj):
    fig=Square(5)
    for f in figure_incorrect_obj:
        with pytest.raises(NotImplementedError) as e:
            fig.add_area(f)
        if "Incorrect class figure" in str(e):
            continue
        else:                                        
            assert False
    assert True
#Треугольник
def test_exception_triangle(figure_incorrect_obj):
    fig=Triangle(7,7,7)
    for f in figure_incorrect_obj:
        with pytest.raises(NotImplementedError) as e:
            fig.add_area(f)
        if "Incorrect class figure" in str(e):
            continue
        else:
            assert False
    assert True
#Проверка атрибута name на известные значения
def test_figure_names(figure_obj_names):
    names_count=len(figure_obj_names)
    names=0
    for fig in figure_obj_names:
       if fig == 'Circle' or fig == 'Triangle' or fig == 'Square' or fig == 'Rectangle':
           names+=1
    assert names == names_count