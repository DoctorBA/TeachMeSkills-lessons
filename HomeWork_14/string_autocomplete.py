#include tables
from model_filling_tables import *


def autocomplete() -> None:
    #Creating fields table Regions     
    reg_brest = Regions.create(region_name='Брестский') 
    reg_vitebsk = Regions.create(region_name='Витебский') 
    reg_grodno = Regions.create(region_name='Гродненский')
    reg_gomel =  Regions.create(region_name='Гомельский')
    reg_minsk = Regions.create(region_name='Минский')
    reg_brest.save()

    #Creating fields table Countries     
    coun_brest = Countries.create(country_name='Брестская', region_id=reg_brest) 
    coun_vitebsk = Countries.create(country_name='Витебская', region_id=reg_vitebsk) 
    coun_grodno = Countries.create(country_name='Гродненская', region_id=reg_grodno)
    coun_gomel =  Countries.create(country_name='Гомельская', region_id=reg_gomel)
    coun_minsk = Countries.create(country_name='Минская', region_id=reg_minsk)

    #Creating fields table Locations     
    loc_brest = Locations.create(street_address='Винника, 51',
                                postal_code='2000',
                                city = 'Брест',
                                state_province='',
                                country_id=coun_brest) 
    loc_vitebsk = Locations.create(street_address='Садовая, 57',
                                postal_code='2001',
                                city = 'Витебск',
                                state_province='',
                                country_id=coun_vitebsk) 
    loc_grodno = Locations.create(street_address='Клецкова, 11',
                                postal_code='2002',
                                city = 'Гродно',
                                state_province='',
                                country_id=coun_grodno) 
    loc_gomel =  Locations.create(street_address='Ватутина, 17',
                                postal_code='2003',
                                city = 'Гомель',
                                state_province='',
                                country_id=coun_gomel) 
    loc_minsk = Locations.create(street_address='Ольшевского, 20',
                                postal_code='2004',
                                city = 'Минск',
                                state_province='',
                                country_id=coun_minsk) 

    #Creating fields table Departments     
    dep_brest = Departments.create(department_id=1,
                                    department_name='Брестский',
                                    manager_id=1,  
                                    locations_id=loc_brest) 
    dep_vitebsk = Departments.create(department_id=2,
                                    department_name='Витебский',
                                    manager_id=2,  
                                    locations_id=loc_vitebsk)  
    dep_grodno = Departments.create(department_id=3,
                                    department_name='Гродненский',
                                    manager_id=3,  
                                    locations_id=loc_grodno) 
    dep_gomel =  Departments.create(department_id=20,
                                    department_name='Гомельский',
                                    manager_id=4,  
                                    locations_id=loc_gomel) 
    dep_minsk = Departments.create(department_id=30,
                                    department_name='Минский',
                                    manager_id=5,  
                                    locations_id=loc_minsk) 

    #Creating fields table Jobs     
    jobOne = Jobs.create(job_title='Директор',
                        min_salary=10000,  
                        max_salary=12000) 
    jobTwo = Jobs.create(job_title='Специалист 1 категории',
                        min_salary=5000,  
                        max_salary=7000)  
    jobThree = Jobs.create(job_title='Бухгалтер',
                        min_salary=8000,  
                        max_salary=10000) 
    jobFour =  Jobs.create(job_title='Технолог',
                        min_salary=7000,  
                        max_salary=10000) 
    jobFive = Jobs.create(job_title='Специалист 2 категории',
                        min_salary=6000,  
                        max_salary=8000) 

    #Creating fields table Job_hisory     
    job_hisOne = Job_hisory.create(start_date='2020-08-14',
                                end_date='2022-09-14',
                                job_id=jobOne,   
                                department_id=dep_brest) 
    job_hisTwo = Job_hisory.create(start_date='2020-08-18',
                                end_date='2022-12-14',
                                job_id=jobTwo,  
                                department_id=dep_vitebsk)  
    job_hisThree = Job_hisory.create(start_date='2020-04-14',
                                end_date='2022-07-10',
                                job_id=jobThree,  
                                department_id=dep_grodno) 
    job_hisFour =  Job_hisory.create(start_date='2020-09-24',
                                end_date='2022-10-17',
                                job_id=jobFour, 
                                department_id=dep_gomel)
    job_hisFive = Job_hisory.create(start_date='2020-11-05',
                                end_date='2022-12-08',
                                job_id=jobFive,  
                                department_id=dep_minsk)

    #Creating fields table Employees     
    EmplOne = Employees.create(first_name='Ivanovich',
                                    last_name='David',
                                    email="",
                                    phone_number=13465413,
                                    hire_date='2021-05-08',
                                    job_id=jobOne,
                                    salary=12000,
                                    commission_PCT=2000,
                                    manager_id=1,
                                    department_id=dep_brest) 
    EmplTwo = Employees.create(first_name='Petrovich',
                                    last_name='David',
                                    email="",
                                    phone_number=7777,
                                    hire_date='2021-05-10',
                                    job_id=jobTwo,
                                    salary=10000,
                                    commission_PCT=1500,
                                    manager_id=2,
                                    department_id=dep_vitebsk) 
    EmplThree = Employees.create(first_name='Sidorov',
                                    last_name='Andrey',
                                    email='',
                                    phone_number=7453,
                                    hire_date='2021-09-20',
                                    job_id=jobThree,
                                    salary=7000,
                                    commission_PCT=900,
                                    manager_id=3,
                                    department_id=dep_grodno) 
    EmplFour =  Employees.create(first_name='Jordan',
                                    last_name='Arseniy',
                                    email='',
                                    phone_number=5698542,
                                    hire_date='2021-10-15',
                                    job_id=jobFour,
                                    salary=5000,
                                    commission_PCT=750,
                                    manager_id=4,
                                    department_id=dep_gomel) 
    EmplFive = Employees.create(first_name='Borsh',
                                    last_name='Timur',
                                    email='',
                                    phone_number=4546123,
                                    hire_date='2021-11-13',
                                    job_id=jobFive,
                                    salary=1000,
                                    commission_PCT=200,
                                    manager_id=5,
                                    department_id=dep_minsk)
    
    print('Аutocomplete completed.') 