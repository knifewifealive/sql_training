from user_db import UserDataBase

db = UserDataBase()

# Добавление пользователей
db.add_user("mbybin","Марк", "mbybin@gmail.com")
db.add_user("pbybina","Полина", "dontWorryBeHappy@yandex.ru")
db.add_user("ashaposhnik","Антон", "currentlyIAmBusy@yandex.ru")
db.add_user("ibarbakov","Илья", "theWeatherIsNice@yandex.ru")
db.add_user("nsholudkova","Наталья", "allIWantIsMoney@yandex.ru")

# Получение всех пользователей
users = db.get_all_users()
print("Список пользователей: \n")

for user_id, username, name, email in users:
    print(f"ID: {user_id}, Name: {name}, Username: {username}, Email: {email}\n")

db.update_user(1, "iammark", "Mark", "bybinmark@yandex.ru")
db.delete_user(2)

# Получение всех пользователей
users = db.get_all_users()
print("UPD: Список пользователей: \n")

for user_id, username, name, email in users:
    print(f"ID: {user_id}, Name: {name}, Username: {username}, Email: {email}\n")