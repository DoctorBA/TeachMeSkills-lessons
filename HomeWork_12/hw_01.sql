/*Задание 1.
Написать запрос, который будет создавать таблицу с столбцами, соответствующие рисунку 1
(Рисунок в облаке прилагается).
*/

CREATE TABLE PC (
    Code INT PRIMARY KEY,
    model VARCHAR(50),
    speed SMALLINT,
    ram SMALLINT,
    hd REAL,
    cd VARCHAR(10),
    price FLOAT
);