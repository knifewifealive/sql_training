from user_db import UserDataBase

db = UserDataBase()


# Получение всех пользователей
users = db.get_all_users()
print("Список пользователей: \n")

for user_id, username, name, email in users:
    print(f"ID: {user_id}, Name: {name}, Username: {username}, Email: {email}\n")

print(db.find_user_by_name("Марк"))
print(db.find_user_by_name_and_email("Марк", "mbyin@gmail.com"))