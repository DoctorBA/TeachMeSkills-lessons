''' Задача 2.
1) Написать программу, которая будет создавать класс данных из JSON объекта.
2) (Дополнительно): Добавить метод для данного класса, который будет выводить все
поля класса.
'''
import json

#initialization data Json
with open("HomeWork_09/Person.json") as file:
    data = json.load(file)

#initialization class show
class ShowField:

    def show(self):
        print(f'Имя: {self.FirstName}\nФамилия: {self.LastName}\nАдрес:\n', \
        *[f'    {k}: {v}\n' for k, v in self.Address.items()], f'Телефон:', *self.PhoneNumbers)

#initialization class
Person = type('NewPerson', (ShowField,), data)

#instantiation object
person_01 = Person()

#output
person_01.show()