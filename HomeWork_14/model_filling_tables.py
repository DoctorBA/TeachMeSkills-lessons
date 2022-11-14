#include tables
from model_tables import * 


def add_regions() -> None:
    region = input('Enter region name: ').capitalize().strip()
    
    try:
        (Regions
                .select()
                .where(Regions.region_name == region)
                .get())
    except:
        print('Record added')
        Regions.create(region_name=region)
    
    
def add_countries() -> None:
    exist = True
    country = input('Enter country name: ').capitalize().strip()
    region_number = input('Enter region id: ')
    
    try:
        region = (Regions
                    .select()
                    .where(Regions.region_id == int(region_number))
                    .get())
    except:
        print('Record is not added')
        exist = False
        
    if exist:
        print('Record added')
        Countries.create(
                        country_name=country,
                        region_id=region
                        )
    
    
def add_locations() -> None:
    exist = True
    street = input('Enter street name: ').capitalize().strip()
    postal = input('Enter postal name: ').capitalize().strip()
    city = input('Enter city name: ').capitalize().strip()
    province = input('Enter province name: ').capitalize().strip()
    country_number = input('Enter country id: ')
    
    try:
        country = (Countries
                    .select()
                    .where(Countries.country_id == int(country_number))
                    .get())
    except:
        print('Record is not added')
        exist = False
     
    if exist:
        print('Record added')
        Locations.create(
                        street_address=street,
                        postal_code=postal,
                        city=city,
                        state_province=province,
                        country_id=country
                        )    
            
    
def add_departments() -> None:
    exist = True
    name = input('Enter department name: ').capitalize().strip()
    manager_number = input('Enter manager id: ')
    location_number = input('Enter location id: ')
    
    try:
        manager_number = int(manager_number)
        location = (Locations
                    .select()
                    .where(Locations.locations_id == int(location_number))
                    .get())
    except:
        print('Record is not added')
        exist = False
     
    if exist:
        print('Record added')
        Departments.create(
                        department_name=name,
                        manager_id=manager_number,
                        locations_id=location
                        )    
   
   
def add_jobs() -> None:
    exist = True
    job = input('Enter job title: ').capitalize().strip()
    min_salary = input('Enter min salary: ')
    max_salary = input('Enter max salar: ')
    
    try:
        min_salary = float(min_salary)
        max_salary = float(max_salary)
    except:
        print('Record is not added')
        exist = False
     
    if exist:
        print('Record added')
        Jobs.create(
                    job_title=job,
                    min_salary=min_salary,
                    max_salary=max_salary
                    )  
    
    
def add_job_hisory() -> None:
    exist = True
    s_date = input('Enter start date: ')
    e_date = input('Enter end date: ')
    job_number = input('Enter job id: ')
    department_number = input('Enter department id: ')
    
    try:
        job_number = (Jobs
                    .select()
                    .where(Jobs.job_id == int(job_number))
                    .get())
        department_number = (Departments
                    .select()
                    .where(Departments.department_id == int(department_number))
                    .get())        
    except:
        print('Record is not added')
        exist = False
     
    if exist:
        print('Record added')
        Job_hisory.create(
                    start_date=s_date,
                    end_date=e_date,
                    job_id=job_number,
                    department_id=department_number
                    )                     
    
    
def add_employees() -> None:
    exist = True
    f_name = input('Enter first name: ').capitalize().strip()
    l_name = input('Enter last name: ').capitalize().strip()
    eml = input('Enter email: ')
    phone = input('Enter phone number: ')
    hire_date = input('Enter hire date: ')
    job_number = input('Enter job id: ')
    sl = input('Enter salary: ')
    commission = input('Enter commission PCT: ')
    manager = input('Enter manager id: ')
    department_number = input('Enter department id: ')
    
    try:        
        phone = int(phone)
        sl = float(sl)
        commission = float(commission)
        manager = int(manager)
        
        job_number = (Jobs
                    .select()
                    .where(Jobs.job_id == int(job_number))
                    .get())
        department_number = (Departments
                    .select()
                    .where(Departments.department_id == int(department_number))
                    .get())        
    except:
        print('Record is not added')
        exist = False
     
    if exist:
        print('Record added')
        Employees.create(
                    first_name = f_name,
                    last_name = l_name,
                    email = eml,
                    phone_number = phone,
                    hire_date = hire_date,
                    job_id = job_number,
                    salary = sl,
                    commission_PCT = commission,
                    manager_id = manager,
                    department_id = department_number
                    )  