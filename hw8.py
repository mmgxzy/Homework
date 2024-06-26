import sqlite3

connect = sqlite3.connect("Mentor.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR (25) NOT NULL,
        age INT DEFAULT NULL,
        adress TEXT,
        email TEXT,
        mentor_in_the_group VARCHAR (6),
        his_group VARCHAR (6),
        coins INT
        )""")

class GeekMentor:
    def __init__(self):
        self.full_name = None
        self.age = 0
        self.adress = None
        self.email = None
        self.mentor_in_the_group = None
        self.his_group = None
        self.coins = 0

    def register(self):
        full_name = input("введите фио:")
        age = int(input("введите возраст:"))
        adress = input("введите адрес:")
        email = input("введите почту:")
        mentor_in_the_group = input("введите в какой группе ментор:")
        his_group = input("введите свою группу:")
        coins = int(input("введите количество коинов:"))

        cursor.execute(f"SELECT email FROM mentors WHERE email = {email}")
        mentor = cursor.fetchone()

        if mentor:
            print("Already exists - Вы уже проходили регистрацию")

        else:
            cursor.execute(f"""INSERT INTO mentors 
                    (full_name, age, adress, email,mentor_in_the_group, his_group, coins)
                    VALUES ('{full_name}', {age},'{adress}' ,'{email}', '{mentor_in_the_group}', '{his_group}', {coins})""")
            print("Вы успешно прошли регистрацию!")

        connect.commit()

    def all_mentors(self):
        cursor.execute("SELECT * FROM mentors")
        mentors = cursor.fetchall()
        print(mentors)

    def plus_mentor_coins(self):
        id = int(input("Введите id студента: "))
        new_coins = int(input("Введите кол-во коинов: "))

        cursor.execute(f"UPDATE mentors SET coins = coins + {new_coins} WHERE id = {id}")
        self.coins += new_coins
        self.coins = self.coins + new_coins
        connect.commit()

    def minus_mentor_coins(self):
        id = int(input("Введите id студента: "))
        new_coins = int(input("Введите кол-во коинов: "))
        print(new_coins)
        if self.coins < new_coins:
            print(self.coins)
            print("нельзя снимать сумму превышающюю баланс!")
        else:
            cursor.execute(f"UPDATE mentors SET coins = coins - {new_coins} WHERE id = {id}")
            self.coins -= new_coins
            self.coins = self.coins - new_coins
            connect.commit()
            print(True)
    def delete_mentor(self):
        id = int(input("Введите id студента: "))
        cursor.execute(f"DELETE FROM mentors WHERE id = {id}")
        connect.commit()

    def main(self):
        while True:
            print("Выберите действие: ")
            print("""0-Выйти\n1-Регистрация ментора\n2-Инфо всех ментаров\n3-Добавление коинов\n4-Обналичить коины\n5-Удаление ментора\n""")


            choice = int(input("Выберите цифру: "))
            if choice == 0:
                break
            elif choice == 1:
                self.register()
            elif choice == 2:
                self.all_mentors()
            elif choice == 3:
                self.plus_mentor_coins()
            elif choice == 4:
                self.minus_mentor_coins()
            elif choice == 5:
                self.delete_mentor()


mentors = GeekMentor()
mentors.main()
