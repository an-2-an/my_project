CREATE TABLE Студенты
(
id INTEGER,
фамилия CHAR(15),
id_группы INTEGER
);


INSERT INTO Студенты (id, фамилия, id_группы) VALUES
(111, 'Семенов', 1),
(112, 'Петрова', 2),
(114, 'Иванов', 3),
(117, 'Сидоров', 3);

SELECT * FROM Студенты;

CREATE TABLE Группы
(
id INTEGER,
группа CHAR(15),
id_факульт INTEGER
);


INSERT INTO Группы (id, группа, id_факульт) VALUES
(1, 'К-18', 11),
(2, 'К-20', 11),
(3, 'Ф-22', 12);

SELECT * FROM Группы;



CREATE TABLE Факультеты
(
id INTEGER,
факультет CHAR(15)
);


INSERT INTO Факультеты (id, факультет) VALUES
(11, 'КТ'),
(12, 'ФК');

SELECT * FROM Факультеты;


CREATE TABLE Предметы
(
id INTEGER,
предмет CHAR(15)
);


INSERT INTO Предметы (id, предмет) VALUES
(101, 'Физика'),
(102, 'Информатика'),
(103, 'Математика');

SELECT * FROM Предметы;



CREATE TABLE Журнал
(
id_студента INTEGER,
id_предмета INTEGER,
оценка INTEGER
);


INSERT INTO Журнал (id_студента, id_предмета, оценка) VALUES
(111, 101, 60),
(111, 102, 80),
(112, 101, 70),
(112, 102, 90),
(114, 103, 75),
(114, 101, 75),
(117, 102, 85);

SELECT * FROM Журнал;