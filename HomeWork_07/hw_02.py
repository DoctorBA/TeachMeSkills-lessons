"""Задча 2.
1) Сделать функцию которая на вход принимает строку.
2) Анализирует ее исключительно методом '.isdigit()' без доп. библиотек
и переводит строку в число. Функция умеет распозновать отрицательные числа и
десятичные дроби.
"""

#Инициализация функции
def foo(s: str) -> str:
    if s.isdigit():
        return f'Вы ввели положительное целое число: {int(s)}'
    else:
        if s[1:].isdigit():
            return f'Вы ввели отрицательное целое число: {int(s)}'
        else:
            numbers = s.split('.')            
            if len(numbers) > 1:
                if numbers[0].isdigit() and numbers[1].isdigit():
                    return f'Вы ввели положительное дробное число: {float(s)}'
                else:
                    if (numbers[0][1:].isdigit() or len(numbers[0]) < 2)and numbers[1].isdigit():
                        return f'Вы ввели отрицательное дробное число: {float(s)}'
                    else:
                        return f'Вы ввели не корректное число: {s}'                
            else:
                return f'Вы ввели не корректное число: {s}'   

#Ввод числа
s = input('Введите число: ')
#Обработка введенного числа
print(foo(s))