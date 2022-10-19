'''Задача 1
1) Напишите программу с классом Student, в котором есть четыре атрибута: firstName,
lastName, groupNumber и age.
2) Установить им любые значения по умолчанию.
3) Необходимо создать пять методов: getFullName, getAge, getGroupNumber, setNameAge,
setGroupNumber. Метод getFullName нужен для получения данных об полном имени конкретного
студента, метод getAge нужен для получения данных о возрасте конкретного студента,
метод GetGroupNumber нужен для получения данных о номере группы конкретного студента.
Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. 
4) В программе необходимо создать пять экземпляров класса Student,
установить им разные имена, возраст и номер группы.
'''
#Объявление класса
class Student:

    #Инициализация атрибутов класса
    def __init__(self, firstName: str=None, lastName: str=None, groupNumber: int=None, age: int=None):
        self.firstName = firstName
        self.lastName = lastName
        self.groupNumber = groupNumber
        self.age = age

    #Метод getFullName
    def getFullName(self) -> str:
        return f'{self.firstName} {self.lastName}'

    #Метод getAge
    def getAge(self) -> str:
        return self.age

    #Метод getGroupNumber
    def getGroupNumber(self) -> str:
        return self.groupNumber

    #Метод setNameAge
    def setNameAge(self, value: int) -> None:
        self.age = value

    #Метод setGroupNumber
    def setGroupNumber(self, value: int) -> None:
        self.groupNumber = value  

#Объявить 5 экземпляров класса Student
student_one = Student('Иванов', 'Иван', 5, 18)
student_two = Student('Петров', 'Петр', 5, 19) 
student_three = Student('Сидоров', 'Генадий', 5, 20) 
student_four = Student('Альянов', 'Дмитрий', 5, 19) 
student_five = Student('Анисенко', 'Лев', 5, 18)