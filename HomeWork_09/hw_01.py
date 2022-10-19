'''Задача 1.
1) Написать класс, который будет создавать треугольник по трём его сторонам.
2) В класс добавить метод, проверяющий возможность построения данного треугольника.
3) Добавить свойства треугольника (длины его сторон) с помощью @ property.
'''
#Initialization class
class Triangle:

    def __init__(self, x: int, y: int, z: int):
        self._x = x
        self._y = y
        self._z = z

    #adds property
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value  

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value: int):
        self._z = value

    #method declaration Triangle
    def check_triangle(self) -> None:
        if self.x + self.y > self.z and self.x + self.y > self.z and self.x + self.y > self.z:
            print(f"Triangle {self.x}, {self.y}, {self.z} can be built")
        else:
            print(f"Triangle {self.x}, {self.y}, {self.z} cannot be built")                

obj = Triangle(10, 6, 1)   
obj.check_triangle()