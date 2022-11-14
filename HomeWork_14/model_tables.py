#include module 
import peewee 
#include database 
from db_connection import db


#include database Model
class Basemodel(peewee.Model):
    class Meta:
        database = db
        

class Regions(Basemodel):
    region_id = peewee.AutoField()
    region_name = peewee.CharField(25)   
    
    
class Countries(Basemodel):
    country_id = peewee.AutoField()
    country_name = peewee.CharField(40)
    region_id = peewee.ForeignKeyField(Regions,
                                       related_name="countries",
                                       on_delete='cascade',
                                       on_update='cascade')    
    

class Locations(Basemodel):
    locations_id = peewee.AutoField()
    street_address = peewee.CharField(40)
    postal_code = peewee.CharField(12)
    city = peewee.CharField(30)
    state_province = peewee.CharField(25)
    country_id = peewee.ForeignKeyField(Countries,
                                        related_name="locations",
                                        on_delete='cascade',
                                        on_update='cascade')   
    
    
class Departments(Basemodel):
    department_id = peewee.AutoField()
    department_name = peewee.CharField(30)
    manager_id = peewee.IntegerField()  
    locations_id = peewee.ForeignKeyField(Locations,
                                            related_name="departments",
                                            on_delete='cascade',
                                            on_update='cascade')
    
    
class Jobs(Basemodel):
    job_id = peewee.AutoField()
    job_title = peewee.CharField(35)
    min_salary = peewee.FloatField()
    max_salary = peewee.FloatField()  
    
    
class Job_hisory(Basemodel):
    employee_id = peewee.AutoField()
    start_date = peewee.DateField()
    end_date = peewee.DateField()
    job_id = peewee.ForeignKeyField(Jobs,
                                    related_name="job_history",
                                    on_delete='cascade',
                                    on_update='cascade')   
    department_id = peewee.ForeignKeyField(Departments,
                                            related_name="job_history",
                                            on_delete='cascade',
                                            on_update='cascade')  
    
    
class Employees(Basemodel):
    employee_id = peewee.AutoField()
    first_name = peewee.CharField(20)
    last_name = peewee.CharField(25)
    email = peewee.CharField(20)
    phone_number = peewee.IntegerField()
    hire_date = peewee.DateField()
    job_id = peewee.ForeignKeyField(Jobs,
                                    related_name="employees",
                                    on_delete='cascade',
                                    on_update='cascade')
    salary = peewee.FloatField()
    commission_PCT = peewee.FloatField()
    manager_id = peewee.IntegerField()
    department_id = peewee.ForeignKeyField(Departments,
                                            related_name="employees",
                                            on_delete='cascade',
                                            on_update='cascade') 
    
    
# Job_hisory.drop_table()
# Employees.drop_table()
# Jobs.drop_table()
# Departments.drop_table()
# Locations.drop_table()
# Countries.drop_table()
# Regions.drop_table()

#Create a tables
Regions.create_table()
Countries.create_table()
Locations.create_table()
Departments.create_table()
Jobs.create_table()
Employees.create_table()
Job_hisory.create_table()                 