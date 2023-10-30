import fileinput
import sqlite3

with sqlite3.connect('students.db') as conn:
    cursor = conn.cursor()


    cursor.execute(''' CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            имя TEXT,
            фамилия TEXT,
            год_рождения INTEGER,
            хобби TEXT,
            баллы_за_дз INTEGER
        )''')
    students_data = [
        ("Алексей", "Щербаков", 1995, "Плавание", 12),
        ("Нурлан ", "Сабуров", 1998, "Гитара", 8),
        ("Тамби", "Масаев", 2000, "Хоккей", 15),
        ("Илья", "Макаров", 1997, "Кино", 5),
        ("Эмир", "Кашоков", 1999, "Пейнтбол", 20),
        ("Сергей", "Детков", 1996, "Бег", 7),
        ("Слава", "Комисаренко", 1994, "Баскетбол", 11),
        ("Виктор", "Комаров", 2000, "борьба", 19),
        ("Ваня", "Усовичь", 2001, "Кулинария", 16),
        ("Иван", "Абрамов", 2003, "Рисование", 9)

    ]
    cursor.executemany("INSERT INTO students (имя, фамилия, год_рождения, хобби, баллы_за_дз) VALUES (?, ?, ?, ?, ?)", students_data)

    cursor.execute("SELECT * FROM students WHERE LENGTH(фамилия) > 10")
    long_surnames = cursor.fetchall()
    print("Студенты с фамилией более 10 символов:")
    for student in long_surnames:
        print(student)
    cursor.execute("UPDATE students SET имя = 'genius' WHERE баллы_за_дз > 10")

    cursor.execute("SELECT * FROM students WHERE имя = 'genius'")
    genius_students = cursor.fetchall()
    print("Студенты с баллами за ДЗ больше 10 (genius):")
    for student in genius_students:
       print(student)

    cursor.execute("DELETE FROM students WHERE id % 2 = 0")

