from faker import Faker
import random
import sqlite3

fake = Faker()

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        group_id INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE groups (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE professors (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE subjects (
        id INTEGER PRIMARY KEY,
        name TEXT,
        professor_id INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE grades (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date TEXT
    )
''')

group_ids = [1, 2, 3]
for group_id in group_ids:
    cursor.execute('INSERT INTO groups (id, name) VALUES (?, ?)', (group_id, f'Group {group_id}'))

for _ in range(30):
    cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (fake.name(), random.choice(group_ids)))

for _ in range(3):
    cursor.execute('INSERT INTO professors (name) VALUES (?)', (fake.name(),))

subject_ids = []
for _ in range(5):
    professor_id = random.randint(1, 3)
    cursor.execute('INSERT INTO subjects (name, professor_id) VALUES (?, ?)', (fake.word(), professor_id))
    subject_ids.append(cursor.lastrowid)

for student_id in range(1, 31):
    for subject_id in subject_ids:
        cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)',
                       (student_id, subject_id, random.randint(2, 5), fake.date_this_decade()))

conn.commit()
conn.close()