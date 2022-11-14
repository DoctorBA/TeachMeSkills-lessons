'''Задача 1.
Заполнить таблицы с помощью Peewee.
'''
#include tables
from model_filling_tables import *
#include string autocomplete 
from string_autocomplete import *

add_tables = {
                '0': 'Exit',
                '1': add_regions,
                '2': add_countries,
                '3': add_locations,
                '4': add_departments,
                '5': add_jobs,
                '6': add_job_hisory,
                '7': add_employees,
                '8': autocomplete   
            }

select = add_tables.get(input('''Menu add record:             
                0. Exit
                1. Add region
                2. Add country
                3. Add location
                4. Add department
                5. Add job
                6. Add job hisory
                7. Add employee
                8. Аutocomplete
                ________________
                Select: '''), 'Exit')

if select != 'Exit':
    select()   
else:
    print('Exit the program...') 
    
   
