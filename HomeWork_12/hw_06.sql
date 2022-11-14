/*Задание 6.
Всем ПК дороже 400 долларов поднять цену в два раза
*/

/*SET SQL_SAFE_UPDATES = 0;*/

UPDATE PC
SET price = price*2
WHERE price > 400;