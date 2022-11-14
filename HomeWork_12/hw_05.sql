/*Задание 5.
Вывести цену всех ПК, чей HD меньше 1000 ГБ.
*/

SELECT model, price
FROM PC
WHERE hd < 1000;