import sqlite3
from environs import Env
from model.session import Session
from model.subject import Subject
import os

env = Env()
env.read_env()
DATABASE_NAME = env.str("DATABASE")

print("Database file:", os.path.abspath(DATABASE_NAME))
print("Exists?", os.path.exists(DATABASE_NAME))

def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DATABASE_NAME)


def initialize_database(connection: sqlite3.Connection) -> None:
    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT NOT NULL,
        subject_lector TEXT NOT NULL,
        subject_study_points INTEGER
    );
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        session_id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_date TEXT NOT NULL,
        session_duration INTEGER NOT NULL,
        subject_id INTEGER NOT NULL,
        FOREIGN KEY(subject_id) REFERENCES subjects(subject_id)
    );
    """)

    connection.commit()

   