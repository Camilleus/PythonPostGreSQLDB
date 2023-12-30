from models import Session, Student, Group, Professor, Subject, Grade
from sqlalchemy import func


def select_1(session):
    # 5 studentów z najwyższą średnią ocen ze wszystkich przedmiotów.
    result = (
        session.query(Student.name, func.avg(Grade.value).label('average'))
        .join(Grade, Student.id == Grade.student_id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.value).desc())
        .limit(5)
        .all()
    )
    return result

def select_2(session, subject_name):
    # Student z najwyższą średnią ocen z określonego przedmiotu.
    result = (
        session.query(Student.name, func.avg(Grade.value).label('average'))
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Student.id)
        .order_by(func.avg(Grade.value).desc())
        .first()
    )
    return result

def select_3(session, subject_name):
    # Średni wynik w grupach dla określonego przedmiotu.
    result = (
        session.query(Group.name, func.avg(Grade.value).label('average'))
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Group.id)
        .all()
    )
    return result

def select_4(session):
    # Średni wynik w grupie (w całej tabeli ocen).
    result = (
        session.query(func.avg(Grade.value).label('average'))
        .scalar()
    )
    return result

def select_5(session, professor_name):
    # Przedmioty, których uczy określony wykładowca.
    result = (
        session.query(Subject.name)
        .join(Grade, Subject.id == Grade.subject_id)
        .join(Professor, Grade.professor_id == Professor.id)
        .filter(Professor.name == professor_name)
        .distinct()
        .all()
    )
    return result

def select_6(session, group_name):
    # Lista studentów w określonej grupie.
    result = (
        session.query(Student.name)
        .join(Group, Student.group_id == Group.id)
        .filter(Group.name == group_name)
        .all()
    )
    return result

def select_7(session, group_name, subject_name):
    # Oceny studentów w określonej grupie z danego przedmiotu.
    result = (
        session.query(Student.name, Grade.value)
        .join(Group, Student.group_id == Group.id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Group.name == group_name, Subject.name == subject_name)
        .all()
    )
    return result

def select_8(session, professor_name):
    # Średnia ocena wystawiona przez określonego wykładowcę z jego przedmiotów.
    result = (
        session.query(func.avg(Grade.value).label('average'))
        .join(Professor, Grade.professor_id == Professor.id)
        .filter(Professor.name == professor_name)
        .scalar()
    )
    return result

def select_9(session, student_name):
    # Lista przedmiotów zaliczonych przez danego studenta.
    result = (
        session.query(Subject.name)
        .join(Grade, Subject.id == Grade.subject_id)
        .join(Student, Grade.student_id == Student.id)
        .filter(Student.name == student_name, Grade.value >= 3)
        .distinct()
        .all()
    )
    return result

def select_10(session, professor_name, student_name):
    # Lista kursów prowadzonych przez określonego wykładowcę dla określonego studenta.
    result = (
        session.query(Subject.name)
        .join(Grade, Subject.id == Grade.subject_id)
        .join(Professor, Grade.professor_id == Professor.id)
        .join(Student, Grade.student_id == Student.id)
        .filter(Professor.name == professor_name, Student.name == student_name)
        .distinct()
        .all()
    )
    return result

def select_11(session, professor_name, student_name):
    # Średnia ocena, jaką określony wykładowca wystawił pewnemu studentowi.
    result = (
        session.query(func.avg(Grade.value).label('average'))
        .join(Student, Grade.student_id == Student.id)
        .join(Subject, Grade.subject_id == Subject.id)
        .join(Professor, Grade.professor_id == Professor.id)
        .filter(Professor.name == professor_name, Student.name == student_name)
        .group_by(Professor.id, Student.id)
        .first()
    )
    return result

def select_12(session, group_name, subject_name):
    # Oceny studentów w określonej grupie z określonego przedmiotu na ostatnich zajęciach.
    result = (
        session.query(Student.name, Grade.value)
        .join(Group, Student.group_id == Group.id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Group.name == group_name, Subject.name == subject_name)
        .order_by(Grade.created_at.desc())
        .all()
    )
    return result

select_functions = {
    '1': select_1,
    '2': select_2,
    '3': select_3,
    '4': select_4,
    '5': select_5,
    '6': select_6,
    '7': select_7,
    '8': select_8,
    '9': select_9,
    '10': select_10,
    '11': select_11,
    '12': select_12,
}

def is_database_empty(session):
    return session.query(func.count('*')).select_from(Student).scalar() == 0

if is_database_empty(Session):
    print("Database is empty. Please run the seed script first.")
else:
    my_select = input("Choose a query (1-12): ")

    try:
        my_select = int(my_select)
        if 1 <= my_select <= 12:
            result = select_functions[str(my_select)](Session)
            print(result)
        else:
            print("Invalid choice. Please choose a valid query number (1-12).")
    except ValueError:
        print("Invalid input. Please enter a number.")