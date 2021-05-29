from abc import ABC
from abc import abstractmethod
class Shape(ABC):
    __color = 'black'
    @abstractmethod
    def calculate_area(self):
        pass
    def __add__(self, other):
        if isinstance(other,(int,float)):
            return f'Summa {self.area + other}'
    def __mul__(self, other):
        if isinstance(other,(int,float)):
            return f'Proizvedenie {self.area * other}'
    def __sub__(self, other):
        if isinstance(other,(int,float)):
                other < self.area
                sub = self.area - other
                print(f'Raznost {sub}')
        else:
            raise ArithmeticError

        def __eq__(self, other):
            if self.area == 0 or other.area == 0:
                self.calculate_area()
                other.calculate_area()
                return self.area == other.area
            else:
                return self.area == other.area

class Rectangle(Shape):
    def __init__(self,length,height,color):
        self.length = length
        self.height = height
        self.area = self.length * self.height
        self.__color = color
    def calculate_area(self):
        self.area = self.length * self.height
        return f'Площадь фигуры:{self.area}\nЦвет:{self.__color}'

class Triangle(Shape):
    def __init__(self,length,height,color = 'black'):
        self.length = length
        self.height = height
        self.__color = color
    def calculate_area(self):
        self.area = self.length*self.height/2
        return f'Площадь фигуры:{self.area}\nЦвет:{self.__color}'

class Circle(Shape):
    def __init__(self,radius,color = 'black'):
        self.__color = color
        self.radius = radius
    def calculate_area(self):
        pi = 3.14
        self.area = pi*self.radius**2
        return f'Площадь фигуры:{self.area}\nЦвет:{self.__color}'


c = Circle(15,'yellow')
print(c.calculate_area())
t = Triangle(10,10)
print(t.calculate_area())
r = Rectangle(12,14,'red')
print(r.calculate_area())
print(r.__add__(15))
print(c.__mul__(2))
print(t.__sub__(100))