from typing import Optional
from pydantic import BaseModel
from db import conn, cursor

class User(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """
        cursor.execute(sql)
        conn.commit()

    def validate(self):
        if not self.first_name or not self.last_name or not self.email or not self.password or not self.confirm_password:
            raise ValueError("All fields are required")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValueError("Invalid email format")

        if self.password!= self.confirm_password:
            raise ValueError("Passwords do not match")

        if len(self.password) < 8:
            raise ValueError("Password must be at least 8 characters long")

    def save(self):
        sql = f"""
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (?,?,?,?)
        """
        cursor.execute(sql, (self.first_name, self.last_name, self.email, self.password))
        conn.commit()
        self.id = cursor.lastrowid
        return self

    @classmethod
    def find_by_email(cls, email: str):
        cursor.execute(f"SELECT * FROM users WHERE email=?", (email,))
        row = cursor.fetchone()
        return cls(**dict(zip([column[0] for column in cursor.description], row))) if row else None

    @classmethod
    def find_by_email_and_password(cls, email: str, password: str):
        cursor.execute(f"SELECT * FROM users WHERE email=? AND password=?", (email, password))
        row = cursor.fetchone()
        return cls(**dict(zip([column[0] for column in cursor.description], row))) if row else None