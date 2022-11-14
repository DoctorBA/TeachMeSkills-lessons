'''Задача 1.
Необходимо создать таблицы 1 и 2 в вашей БД с помощью ORM Peewee. (Таблицы на диске)
'''

#include module 
import peewee 
#include database 
from db_connection import db


class Part(peewee.Model):
    Part_ID = peewee.AutoField()
    Part = peewee.CharField(50) 
    Cat = peewee.IntegerField()
    
    
    class Meta:
        database = db
        db_table = "part"
        
        
class Cat(peewee.Model):
    Catnumb = peewee.IntegerField(primary_key=True)
    Cat_name = peewee.CharField(50) 
    Price = peewee.FloatField()
    
    
    class Meta:
        database = db
        db_table = "cat"
        
            
#Create a tables
Part.create_table()
Cat.create_table()       
      
#Creating fields table Part        
Part.create(Part='Квартиры', Cat=505)     
Part.create(Part='Автомашины', Cat=205)
Part.create(Part='Доски', Cat=10)
Part.create(Part='Шкафы', Cat=30)
Part.create(Part='Книги', Cat=160)

#Creating fields table Cat 
Cat.create(Catnumb=10, Cat_name="Стройматериалы", Price=105.00)  
Cat.create(Catnumb=505, Cat_name="Недвижимость", Price=210.00) 
Cat.create(Catnumb=205, Cat_name="Транспорт", Price=160.00) 
Cat.create(Catnumb=30, Cat_name="Мебель", Price=77.00) 
Cat.create(Catnumb=45, Cat_name="Техника", Price=65.00)  
