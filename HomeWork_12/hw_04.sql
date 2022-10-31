/*Задание 4.
Найти номер модели, скорость и размер жесткого диска ПК, имеющий RAM от 8 до 16 ГБ.
*/

SELECT model, speed, hd
FROM PC
WHERE ram BETWEEN 8 AND 16;