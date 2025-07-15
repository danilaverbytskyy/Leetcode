create table fine(
    fine_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30),
    number_plate VARCHAR(6),
    violation VARCHAR(50),
    sum_fine DECIMAL(8, 2),
    date_violation date,
    date_payment date
);

INSERT INTO fine(name, number_plate, violation, sum_fine, date_violation, date_payment)
VALUES
    ('Баранов П.Е.','Р523ВТ','Превышение скорости
(от 40 до 60)', null,'2020-02-14', null),
    ('Абрамова К.А.','О111АВ','Проезд на
запрещающий сигнал',null, '2020-02-23', null),
    ('Яковлев Г.Р.','Т330ТТ','Проезд на
запрещающий сигнал',null, '2020-03-03', null)