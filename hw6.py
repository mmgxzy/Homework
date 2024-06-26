import sqlite3

connect = sqlite3.connect("pubg.db")
cursor = connect.cursor()

cursor.execute("""  
CREATE TABLE IF NOT EXISTS player(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    your_username VARCHAR (15), 
    birth_date DATE,        
    player_name VARCHAR (10),
    gender VARCHAR (7),
    server TEXT
    )""")

def register():
    your_username = input("введите имя пользователя:")
    birth_date = input("введите дату рождения:")
    server = input("укажите сервер:")
    player_name = input("веддите имя персонажа:")
    gender = input("выберите пол персонажа:")
    server = input("укажите сервер:")

    cursor.execute(f"""INSERT INTO player 
               (your_username, birth_date, gender, server, player_name)
                VALUES ('{your_username}', '{birth_date}', '{server}', '{player_name}','{ gender}')""")
    
    connect.commit()

register()


def player():
    start = int(input('Начать игру? да - 1, нет - 2\n'))
    
    if start == 1:
        print("игра началась!")  
    elif start == 2: 
        print("игра приостановлена!")
    else:
        print("такой команды нет!")

def playing():
    imposter = int(input("враг впереди! 1 - срелять, 2 - убежать\n"))
    if imposter == 1:
        print("враг умер.")
    elif imposter == 2:
        print("враг бежит за вами!")
    else:
        print("такой команды нет!")

def comands():
    you = int(input("вы вошли в дом 1 - сесть, 2 - прыгнуть\n"))
    if you == 1:
        print("вы седите.")
    elif you == 2:
        print("вы прыгнули!")
    else:
        print("такой команды нет!")

def kill():
    killing = int(input("враг за окном! 1 - стрелять, 2 - ждать\n"))
    if killing == 1:
        print("враг умер. игра окончена!")
    elif killing == 2:
        print("вы ждете! убить не судьба?")
    else:
        print("такой команды нет!")
   
    


player()
playing()
comands()  
kill()


    # cursor.execute("SELECT * FROM player")
    # player = cursor.fetchall()
    # print(player)



