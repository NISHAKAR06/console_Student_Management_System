import sqlite3

class DBManager:
    def __init__(self, db_name="students.db"):
        self.db_name = db_name
        self._create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                course TEXT
            )
        """)
        conn.commit()
        conn.close()

    def execute(self, query, params=(), fetch=False, fetchone=False):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(query, params)
        result = None
        if fetch:
            result = cur.fetchall()
        elif fetchone:
            result = cur.fetchone()
        conn.commit()
        conn.close()
        return result
