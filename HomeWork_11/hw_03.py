'''Задача 3.
Написать регулярное выражение, которое будет проверять формат времени.
(14:00 - True, 25:66 - False)
'''
#include module 
import re

'''First way:'''

#input hours and minutes
hours = input('Enter hours: ')
minutes = input('Enter minutes: ')

#regular expression for hours and minutes
reg_hours = r"[0-1][0-9]|[2][0-3]"
reg_minutes  = r"[0-5][0-9]"

match_hours = re.fullmatch(reg_hours, hours)
match_minutes = re.fullmatch(reg_minutes, minutes)

#output result
print(True if match_hours and match_minutes else False)  

'''Second way:'''

#input time
time = input('Enter time in the format h/m "__:__": ')

#regular expression for time
reg_time = r"([0-1][0-9]|[2][0-3]):[0-5][0-9]"

match_time = re.fullmatch(reg_time, time)

#output result
print(True if match_time else False)  