'''Задача 4.
Написать программу, которая должна определить город по почтовому индексу.
(Возьмите города РБ, можно только областные).
Например: (246028 - Гомель, 220004 - Минск).
Использовать регулярные выражения.
'''
#include module 
import re

city_index = {
    '220000': 'Minsk', '224000': 'Brest', '210000': 'Vitebsk',
    '246000': 'Gomel', '230000': 'Grodno', '212000': 'Mogilev'
    }

'''Условие 1) Определяет Город по введенному адресу'''

#input address
address = input('Enter your address: ')

#regular expression for index
index = r"\b\d{6}\b"

match_index = re.search(index, address)

#output result
print(city_index.setdefault(match_index[0], f'City not found or invalid address'))

'''Условие 2) Определяет Города по введенным индексам'''

#input address
indexes = input('Enter indexes city: ')

#regular expression for index
reg_index = r"\b\d{6}\b"

match_indexs = re.findall(reg_index, indexes)

#output result
for idx in match_indexs:  
    print(f'{idx} - {city_index.setdefault(idx, f"City not found or invalid address")}')

