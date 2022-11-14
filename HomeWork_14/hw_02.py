'''Задача 2.
a) Таблица Employees. Получить список всех сотрудников из 20го и из 30го
отдела (department_id).
b) Таблица Employees. Получить список всех сотрудников с именем 'David'.
c) Таблица Employees. Получить список всех сотрудников которые пришли
на работу в феврале 2021го года.
'''
#include tables
from model_tables import * 


#output result
def out_query(query: dict) -> None:
    print(
            'First_name'.center(12),
            'Last_name'.center(12),
            'Email'.center(10),
            'Phone_number'.center(15),
            'Hire_date'.center(12),
            'Salary'.center(8),
            'Commission_PCT'.center(10),
            sep='|'
        )

    for result in query:
        print(
                str(result["first_name"]).center(12),
                str(result["last_name"]).center(12),
                str(result["email"]).center(10),
                str(result["phone_number"]).center(15),
                str(result["hire_date"]).center(12), 
                str(result["salary"]).center(8),
                str(result["commission_PCT"]).center(10),
                sep='|'
            )


#Task a.
print("Task a:")
task_a = (Employees
                .select(
                        Employees.first_name,
                        Employees.last_name,
                        Employees.email,
                        Employees.phone_number,
                        Employees.hire_date,
                        Employees.salary,
                        Employees.commission_PCT                        
                    )
                .where((Employees.department_id == 20) |
                       (Employees.department_id == 30))
                .dicts())

out_query(task_a)
print('_________')

#Task b.
print("Task b:")
task_b = (Employees
                .select(
                        Employees.first_name,
                        Employees.last_name,
                        Employees.email,
                        Employees.phone_number,
                        Employees.hire_date,
                        Employees.salary,
                        Employees.commission_PCT                        
                    )
                .where(Employees.last_name == 'David')
                .dicts())

out_query(task_b)
print('_________')

#Task c.
print("Task c:")
task_c = (Employees
                .select(
                        Employees.first_name,
                        Employees.last_name,
                        Employees.email,
                        Employees.phone_number,
                        Employees.hire_date,
                        Employees.salary,
                        Employees.commission_PCT                        
                    )
                .where((Employees.hire_date.year == '2021') &
                       (Employees.hire_date.month == '02'))
                .dicts())

out_query(task_c)