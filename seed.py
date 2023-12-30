import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Session, Student, Group, Professor, Subject, Grade

fake = Faker()

def create_students(session, num_students):
    students = []
    for _ in range(num_students):
        student = Student(
            name=fake.name(),
            email=fake.email(),
            group_id=random.choice(session.query(Group.id).all())[0]
        )
        students.append(student)
        session.add(student)
    session.commit()
    
def create_groups(session, num_groups):
    groups = []
    for _ in range(num_groups):
        group = Group(name=fake.word())
        groups.append(group)
        session.add(group)
    session.commit()
    
def create_subjects(session, num_subjects):
    subjects = []
    for _ in range(num_subjects):   
        subject = Subject(name=fake.word())
        subjects.append(subject)
        session.add(subject)
    session.commit()
    
def create_professors(session, num_professors):
    professors = []
    for _ in range(num_professors):
        professor = Professor(name=fake.name())
        professors.append(professor)
        session.add(Professor)
    session.commit()
    
def create_grades(session, num_grades):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    professors = session.query(Professor).all()

    for _ in range(num_grades):
        grade = Grade(
            value=random.randint(2, 5),
            student_id=random.choice(students).id,
            subject_id=random.choice(subjects).id,
            Professor_id=random.choice(professors).id
        )
        session.add(grade)
    session.commit()

db_username = 'Camilleus'
db_password = 'J3St3MM1L10N3R3M'
db_host = 'localhost'
db_port = '5432'
db_name = 'PythonPostGresV1'

engine = create_engine(f'postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

Session = sessionmaker(bind=engine)
session = Session()

create_groups(session, 3)
create_subjects(session, 8)
create_professors(session, 5)
create_students(session, 30)
create_grades(session, 20)

session.close()