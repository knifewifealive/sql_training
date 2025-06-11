import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect('database/users.db')
cursor = conn.cursor()

# Создание таблицы users, если она не существует
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE)
    """
)

# Сохраниние изменений и закрытие соединения
conn.commit()
conn.close()