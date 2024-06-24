"БД - База Данных"
"СУБД - Система Управления Базой Данных"
"CRUD - Create, Reade, Update, Delete"

import sqlite3

connect = sqlite3.connect("Geeks.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR (30),
        age INT,
        is_have BOOLEAN,
        direction TEXT,
        rating DOUBLE (4,2),
        birth_date DATE
        )""")


def register():
    full_name = input("Введите ФИО: ")
    age = int(input("Введите возраст: "))
    is_have = bool(input("Наличие ноутбука: "))
    direction = input("Введите направление: ")
    rating = float(input("Введите свой рейтинг: "))
    birth_date = input("Введите дату рождения: ")

    # cursor.execute("""INSERT INTO students 
    #                (full_name, age, is_have, direction, rating, birth_date)
    #                VALUES ('?', ?, ?, '?', ?, '?')""", full_name, age, is_have, direction, rating, birth_date)


    cursor.execute(f"""INSERT INTO students 
                   (full_name, age, is_have, direction, rating, birth_date)
                   VALUES ('{full_name}', {age}, {is_have}, '{direction}', {rating}, '{birth_date}')""")

    connect.commit()

def all_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print(students)

all_students()
# register()