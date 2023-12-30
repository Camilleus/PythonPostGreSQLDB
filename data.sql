/*students*/
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    group_id INTEGER
);

INSERT INTO students (student_id, name, group_id) VALUES
(1, 'James Krasicki', 1),
(2, 'Emily Nowak', 2),
(3, 'Michael Wojcik', 1),
(4, 'Olivia Dabrowski', 3),
(5, 'Liam Kowalczyk', 2),
(6, 'Sophia Kaminski', 1),
(7, 'Jacob Lewandowski', 3),
(8, 'Emma Lukasiewicz', 2),
(9, 'Mia Wojciechowski', 1),
(10, 'Noah Kaminski', 3),
(11, 'Ava Kowal', 2),
(12, 'Isabella Zajac', 1),
(13, 'William Szymanski', 3),
(14, 'Amelia Wozniak', 2),
(15, 'Alexander Duda', 1),
(16, 'Daniel Mazur', 3),
(17, 'Grace Pawlowski', 2),
(18, 'Henry Zalewski', 1),
(19, 'Avery Krol', 3),
(20, 'Oliver Majewski', 2),
(21, 'Scarlett Nowicki', 1),
(22, 'Sebastian Kaczmarek', 3),
(23, 'Lily Piotrowski', 2),
(24, 'Zachary Jasinski', 1),
(25, 'Abigail Grabowski', 3),
(26, 'Christopher Nowacki', 2),
(27, 'Hannah Sikora', 1),
(28, 'Camilleus Rex', 3),
(29, 'August Leon', 3),
(30, 'Matthias El Guerriero', 3);


/*subjects*/
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY,
    name TEXT,
    professor_id INTEGER
);

INSERT INTO subjects (subject_id, name, professor_id) VALUES
(1, 'Mathematics', 1),
(2, 'History', 2),
(3, 'Computer Science', 3),
(4, 'Worldwide Literature', 4),
(5, 'Polish Literature', 5),
(6, 'Physics', 6),
(7, 'Biology', 7),
(8, 'Geography', 8),
(9, 'Chemistry', 9),
(10, 'Grammary', 10);


/*groups*/
CREATE TABLE groups (
    group_id INTEGER PRIMARY KEY,
    name TEXT
);

INSERT INTO groups (group_id, name) VALUES
(1, 'Grupa 1'),
(2, 'Grupa 2'),
(3, 'Grupa 3');


/*professors*/
CREATE TABLE professors (
    professor_id INTEGER PRIMARY KEY,
    name TEXT
);

INSERT INTO professors (professor_id, name) VALUES
(1, 'Profesor Adamowicz'),
(2, 'Profesor Bialkowski'),
(3, 'Profesor Czajkowski'),
(4, 'Profesor Dabrowski'),
(5, 'Profesor Ejsmont');


/*grades*/
CREATE TABLE grades (
    grade_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date TEXT
);

INSERT INTO grades (student_id, subject_id, grade, date) VALUES
(1, 1, 4, '2023-01-15'),
(1, 2, 5, '2023-02-20'),
(1, 3, 3, '2023-03-10'),
(2, 1, 3, '2023-04-05'),
(2, 3, 4, '2023-05-01'),
(2, 5, 5, '2023-06-15'),
(3, 1, 5, '2023-07-02'),
(3, 2, 4, '2023-08-10'),
(3, 3, 5, '2023-09-22');
