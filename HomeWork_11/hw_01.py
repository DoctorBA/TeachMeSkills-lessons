'''Задача 1.
Числа Фибоначчи представляют последовательность, получаемую в результате сложения
двух предыдущих элементов. Начинается коллекция с чисел 1 и 1. Она
достаточно быстро растет, поэтому вычисление больших значений занимает немало времени.
Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными
затратами ресурсов.
Для реализации этой функции потребуется обратиться к инструкции yield. Она не сохраняет
в оперативной памяти огромную последовательность, а дает возможность
"доставать" промежуточные результаты по одному.
________________________________
Решить Задачу используя итератор.
'''
#initialization function Fibonacci
def fib_iter(n: int) -> list:
    result = [1]
    if n > 1:
        result = [1, 1]
        for value in range(n-2):
            result += [result[value]+result[value+1]]               
    return result   

n = 10
#call function     
print(fib_iter(n))

#initialization class Fibonacci
class fib:
    
    def __init__(self, num: int):
        self.result = self.fib(num)
        
    #returns an iterator Fibonacci list    
    @staticmethod     
    def fib(num: int) -> iter:
        result = [1]
        if num > 1:
            result = [1, 1]
            for value in range(num-2):
                result += [result[value]+result[value+1]]               
        return iter(result)            

    def __iter__(self):
        return self.result
    
    def __next__(self):
        return next(self.result)

#instantiation object iterator Fibonacci
iterator = fib(5)

print(next(iterator))
print(next(iterator))

for i in iterator:
    print(i, end= ' ')

