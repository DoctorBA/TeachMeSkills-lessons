/*Задача 2.
Реализовать следующий SQL-запрос: соединить данные двух таблиц так,
чтобы данные пересекались по криттерию Cat и Catnumb. (Выполнить все JOIN)
*/

/*LEFT JOIN INCLUSIVE*/
SELECT *
FROM Part
	LEFT JOIN Cat ON Part.Cat = Cat.Catnumb;

/*LEFT JOIN EXCLUSIVE*/   
SELECT *
FROM Part
	LEFT JOIN Cat ON Part.Cat = Cat.Catnumb
WHERE  Cat.Catnumb IS NULL;   

/*INNER JOIN*/  
SELECT *
FROM Part
	INNER JOIN Cat ON Part.Cat = Cat.Catnumb;

/*RIGHT JOIN INCLUSIVE*/ 
SELECT *
FROM Part
	RIGHT JOIN Cat ON Part.Cat = Cat.Catnumb;       

/*RIGHT JOIN EXCLUSIVE*/  
SELECT *
FROM Part
	RIGHT JOIN Cat ON Part.Cat = Cat.Catnumb
WHERE Part.Cat IS NULL;  

/*FULL OUTER INCLUSIVE*/  
SELECT *
FROM Part
LEFT JOIN Cat ON Part.Cat = Cat.Catnumb

UNION ALL

SELECT *
FROM Part
RIGHT JOIN Cat ON Part.Cat = Cat.Catnumb
WHERE Part.Cat IS NULL;

/*FULL OUTER EXCLUSIVE*/ 
SELECT *
FROM Part
LEFT JOIN Cat ON Part.Cat = Cat.Catnumb
WHERE Cat.Catnumb IS NULL

UNION ALL

SELECT *
FROM Part
RIGHT JOIN Cat ON Part.Cat = Cat.Catnumb
WHERE Part.Cat IS NULL;
