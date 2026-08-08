import random
from pathlib import Path
from sqlalchemy import ForeignKey, create_engine, select
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    relationship,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship
DB_PATH = Path(__file__).resolve().parent / "students.db"
class Base(DeclarativeBase):
    pass
# Проміжна таблиця для зв'язку "багато до багатьох":
# один студент може бути на кількох курсах, на курсі — багато студентів.
class StudentCourse(Base):
    __tablename__ = "student_course"
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), primary_key=True)
class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    courses: Mapped[list["Course"]] = relationship(
        secondary="student_course", back_populates="students"
    )
class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    students: Mapped[list["Student"]] = relationship(
        secondary="student_course", back_populates="courses"
    )
engine = create_engine(f"sqlite:///{DB_PATH}")
# Створюємо базу з нуля, щоб результат був відтворюваним при кожному запуску.
engine = create_engine("sqlite:///students.db")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
# ==========================================
# 1. Створення моделі даних: 5 курсів і 20 студентів (розподіл рандомний)
# ==========================================
course_titles = ["Python", "SQL", "Git", "Linux", "Automation QA"]
student_names = [
    "Ivan", "Anna", "Petro", "Olena", "Serhii", "Maria", "Andrii", "Kateryna",
    "Dmytro", "Sofia", "Oleg", "Nadia", "Taras", "Yulia", "Roman", "Iryna",
    "Vadym", "Oksana", "Bohdan", "Halyna",
]
with Session(engine) as session:
    courses = [Course(title=title) for title in course_titles]
    session.add_all(courses)
    for name in student_names:
        student = Student(name=name)
        # кожен студент потрапляє випадково на 1-3 курси
        student.courses = random.sample(courses, random.randint(1, 3))
        session.add(student)
    session.commit()
print("1. Створено", len(course_titles), "курсів і", len(student_names), "студентів (рандомний розподіл)")
# ==========================================
# 2. Базові операції: додати нового студента й записати на курс
# ==========================================
with Session(engine) as session:
    python_course = session.scalar(select(Course).where(Course.title == "Python"))
    new_student = Student(name="Volodymyr")
    new_student.courses.append(python_course)
    session.add(new_student)
    session.commit()
    print(f"Додано студента {new_student.name} на курс {python_course.title}")
    print(f"\n2. Додано студента '{new_student.name}' і записано на курс '{python_course.title}'")
# ==========================================
# 3. Запити: студенти певного курсу та курси певного студента
# ==========================================
with Session(engine) as session:
    python_course = session.scalar(select(Course).where(Course.title == "Python"))
    print(f"\n3. Студенти на курсі '{python_course.title}':")
    print(f"\nСтуденти на курсі {python_course.title}:")
    for student in python_course.students:
        print("   -", student.name)
        print(" -", student.name)
    volodymyr = session.scalar(select(Student).where(Student.name == "Volodymyr"))
    print(f"\n   Курси студента '{volodymyr.name}':")
    print(f"\nКурси студента {volodymyr.name}:")
    for course in volodymyr.courses:
        print("   -", course.title)
        print(" -", course.title)
# ==========================================
# 4. Оновлення та видалення
# ==========================================
with Session(engine) as session:
    # оновлюємо ім'я студента
    volodymyr = session.scalar(select(Student).where(Student.name == "Volodymyr"))
    volodymyr.name = "Volodymyr Melnyk"
    # оновлюємо назву курсу
    sql_course = session.scalar(select(Course).where(Course.title == "SQL"))
    sql_course.title = "SQL Basics"
    session.commit()
    print(f"\n4. Оновлено: студент -> '{volodymyr.name}', курс -> '{sql_course.title}'")
    print(f"\nОновлено: {volodymyr.name}, курс {sql_course.title}")
    # видаляємо студента
    student_to_delete = session.scalar(select(Student).where(Student.name == "Ivan"))
    session.delete(student_to_delete)
    ivan = session.scalar(select(Student).where(Student.name == "Ivan"))
    session.delete(ivan)
    session.commit()
    print(f"   Видалено студента 'Ivan'")
    total = session.scalar(select(Student).where(Student.name == "Ivan"))
    print("   Перевірка: студент 'Ivan' у базі —", "відсутній" if total is None else "ще є")
    print("Видалено студента Ivan")
