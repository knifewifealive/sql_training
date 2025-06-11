import sqlite3
from typing import List, Tuple

class UserDataBase:
    def __init__(self, db_path: str = 'database/users.db'):
        self.db_path = db_path
        self._create_table()

    # Подключение к базе данных
    def _connect(self):
        return sqlite3.connect(self.db_path)
    
    #  Cоздание таблицы пользователей
    def _create_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE)
"""
            )
        conn.commit()

    # Добавление пользователя
    def add_user(self, username: str, name: str, email: str) -> None:
        with self._connect() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO users (username, name, email) VALUES (?, ?, ?)", (username,name, email)
                )
                conn.commit()
                print(f"Success: User '{username}' added successfully.")
            except sqlite3.IntegrityError:
                print(f"Error: User with username '{username}' or email '{email}' already exists.")

    def get_all_users(self) -> List[Tuple[int, str, str, str]]:
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, name, email FROM users")
            return cursor.fetchall()