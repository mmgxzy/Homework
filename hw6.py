import sqlite3

connect = sqlite3.connect("pubg.db")
cursor = connect.cursor()

cursor.execute("""  
CREATE TABLE IF NOT EXISTS player(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    your_username VARCHAR (15), 
    birth_date DATE,        
    player_name VARCHAR (10),
    height DOUBLE (5,2),
    gender BOOLEAN,
    server TEXT
    )""")

def register():
    your_username = input("введите имя пользователя:")
    birth_date = input("введите дату рождения:")
    player_name = input("веддите имя персонажа:")
    height = float(input("введите рост персонажа: "))
    gender = bool(input("выберите пол персонажа"))
    server = input("укажите сервер:")

    cursor.execute(f"""INSERT INTO students 
           (your_username, birth_date, player_name, height, gender, server)
           VALUES ('{your_username}', '{birth_date}', '{player_name}', '{height}','{ gender}', '{server}')""")
    
    connect.commit()

def player():
    cursor.execute("SELECT 1 FROM player")
    player = cursor.fetchall()
    print(player)

player()