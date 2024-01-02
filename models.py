from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='student')

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student', back_populates='group')
    
class Professor(Base):
    __tablename__ = 'professors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subjects = relationship('Subject', back_populates='professor')
    
class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    professor_id = Column(Integer, ForeignKey('professors.id'))
    professor = relationship('Professor', back_populates='subjects')
    grades = relationship('Grade', back_populates='subject')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Integer)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    student = relationship('Student', back_populates='grades')
    subject = relationship('Subject', back_populates='grades')


if __name__ == '__main__':
    try:
        engine = create_engine('postgresql://Camilleus:J3st3mM1l1on3r3m@localhost:5432/PythonPostgresV1')
        
        if not engine:
            raise Exception("Failed to create the engine.")

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()


    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if session:
            session.close()