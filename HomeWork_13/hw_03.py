"""Задача 3.
Реализовать такую функцию (SQL-запрос JOIN) в Python с помощью ORM Peewee.
"""

#include module 
from peewee import *
#include database 
from db_connection import db
#include tables
from hw_01 import * 

#output result
def out_query(query: dict) -> None:
    print(
            'Part_ID'.center(10),
            'Part'.center(15),
            'Cat'.center(5),
            'Catnumb'.center(10),
            'Cat_name'.center(20),
            'Price'.center(10),
            sep='|'
        )

    for result in query:
        print(
                str(result["Part_ID"]).center(10),
                str(result["Part"]).center(15),
                str(result["Cat"]).center(5),
                str(result["Catnumb"]).center(10),
                str(result["Cat_name"]).center(20), 
                str(result["Price"]).center(10),
                sep='|'
            )

#LEFT JOIN INCLUSIVE
query_LEFT_JOIN_INCLUSIVE = (Part
                             .select(
                                    Part.Part_ID,
                                    Part.Part,
                                    Part.Cat,
                                    Cat.Catnumb,
                                    Cat.Cat_name,
                                    Cat.Price)
                             .join(Cat, JOIN.LEFT_OUTER, on=(Part.Cat == Cat.Catnumb))
                             .dicts())

#LEFT JOIN EXCLUSIVE
query_LEFT_JOIN_EXCLUSIVE = (Part
                             .select(
                                    Part.Part_ID,
                                    Part.Part,
                                    Part.Cat,
                                    Cat.Catnumb,
                                    Cat.Cat_name,
                                    Cat.Price)
                             .join(Cat, JOIN.LEFT_OUTER, on=(Part.Cat == Cat.Catnumb))
                             .where(Cat.Catnumb == None)
                             .dicts())

#INNER JOIN
query_INNER_JOIN = (Part
                    .select(
                            Part.Part_ID,
                            Part.Part,
                            Part.Cat,
                            Cat.Catnumb,
                            Cat.Cat_name,
                            Cat.Price)
                    .join(Cat, on=(Part.Cat == Cat.Catnumb))
                    .dicts())

#RIGHT JOIN INCLUSIVE
query_RIGHT_JOIN_INCLUSIVE = (Part
                             .select(
                                    Part.Part_ID,
                                    Part.Part,
                                    Part.Cat,
                                    Cat.Catnumb,
                                    Cat.Cat_name,
                                    Cat.Price)
                             .join(Cat, JOIN.RIGHT_OUTER, on=(Part.Cat == Cat.Catnumb))
                             .dicts())

#RIGHT JOIN EXCLUSIVE
query_RIGHT_JOIN_EXCLUSIVE = (Part
                             .select(
                                    Part.Part_ID,
                                    Part.Part,
                                    Part.Cat,
                                    Cat.Catnumb,
                                    Cat.Cat_name,
                                    Cat.Price)
                             .join(Cat, JOIN.RIGHT_OUTER, on=(Part.Cat == Cat.Catnumb))
                             .where(Part.Cat == None)
                             .dicts())

#FULL OUTER INCLUSIVE
query_FULL_OUTER_INCLUSIVEE = ((Part
                             .select(
                                    Part.Part_ID,
                                    Part.Part,
                                    Part.Cat,
                                    Cat.Catnumb,
                                    Cat.Cat_name,
                                    Cat.Price)
                             .join(Cat, JOIN.LEFT_OUTER, on=(Part.Cat == Cat.Catnumb)))
                            .union_all
                             (Part
                             .select(
                                    Part.Part_ID,
                                    Part.Part,
                                    Part.Cat,
                                    Cat.Catnumb,
                                    Cat.Cat_name,
                                    Cat.Price)
                             .join(Cat, JOIN.RIGHT_OUTER, on=(Part.Cat == Cat.Catnumb))
                             .where(Part.Cat == None))    
                             .dicts())

#FULL OUTER EXCLUSIVE
query_FULL_OUTER_EXCLUSIVE = ((Part
                             .select(
                                    Part.Part_ID,
                                    Part.Part,
                                    Part.Cat,
                                    Cat.Catnumb,
                                    Cat.Cat_name,
                                    Cat.Price)
                             .join(Cat, JOIN.LEFT_OUTER, on=(Part.Cat == Cat.Catnumb)))
                             .where(Cat.Catnumb == None)
                             .union_all
                             (Part
                             .select(
                                    Part.Part_ID,
                                    Part.Part,
                                    Part.Cat,
                                    Cat.Catnumb,
                                    Cat.Cat_name,
                                    Cat.Price)
                             .join(Cat, JOIN.RIGHT_OUTER, on=(Part.Cat == Cat.Catnumb))
                             .where(Part.Cat == None))    
                             .dicts())

query_dict = {
                     '0': 'Exit',
                     '1': query_LEFT_JOIN_INCLUSIVE,
                     '2': query_LEFT_JOIN_EXCLUSIVE,
                     '3': query_INNER_JOIN,
                     '4': query_RIGHT_JOIN_INCLUSIVE,
                     '5': query_RIGHT_JOIN_EXCLUSIVE,
                     '6': query_FULL_OUTER_INCLUSIVEE,
                     '7': query_FULL_OUTER_EXCLUSIVE
              }

select_query = query_dict.get(input(f"""Select query:
                            0. Exit
                            1. query_LEFT_JOIN_INCLUSIVE
                            2. query_LEFT_JOIN_EXCLUSIVE
                            3. query_INNER_JOIN
                            4. query_RIGHT_JOIN_INCLUSIVE
                            5. query_RIGHT_JOIN_EXCLUSIVE
                            6. query_FULL_OUTER_INCLUSIVEE
                            7. query_FULL_OUTER_EXCLUSIVE
                            _____________________________
                            Your select: """), 'Exit')

if select_query != 'Exit':
       out_query(select_query)
else:
       print('Exit the program...')       
