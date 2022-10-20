'''Задача 4.
1) Евгения создала класс KgToPounds с параметром kg, куда передается определенное
количество килограмм, а с помощью метода to_pounds() они переводятся в фунты.
2) Чтобы закрыть доступ к переменной “kg” она реализовала методы set_kg() - для задания
нового значения килограммов, get_kg()  - для вывода текущего значения кг.
3) Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода для
задания и вывода значений. Помогите ей переделать класс с использованием функции
property() и свойств-декораторов. Код приведен ниже. 
'''
#include modul
from typing import Union

#main class initialization
class KgToPounds:

    def __init__(self, kg: Union[str, list]):
        self.__kg = kg

    #property check
    def __setattr__(self, key, value):
        if isinstance(value, (float, int)):
            object.__setattr__(self, key, value)
        else:
            raise ValueError('kg are given only by int or float')

    @property
    def kg(self) -> Union[str, list]:
        return self.__kg

    @kg.setter
    def kg(self, value: Union[str, list]):
        self.__kg = value  
    
    #initialization method to_pounds
    def to_pounds(self) -> float:
        return self.kg * round(2.20462262185, 2)           

obj = KgToPounds(123)
print(f'Количество килограмм: {obj.kg}')
print(f'Количество фунтов: {obj.to_pounds()}')