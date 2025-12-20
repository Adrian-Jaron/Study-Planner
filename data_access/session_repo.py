from environs import Env
import sqlite3
from datetime import date, datetime
from model.session import Session
from data_access.connection import get_connection


env = Env()
env.read_env()
DATABASE_NAME = env.str("DATABASE")

def is_valid_date(date_string: str) -> bool:
    try:
            datetime.strptime(date_string, "%Y-%m-%d").date()
            return True
    except (TypeError, ValueError):
            return False
        
def convert_session_row(row: tuple) -> Session:
     return Session(
         id=row[0],
         date=row[1],
         duration=row[2],
         subject_id=row[3]
         )
 
def get_all_sessions() -> list[Session]:
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sessions order by session_date DESC")
        rows = cursor.fetchall()
        return [convert_session_row(row) for row in rows]
    
def get_session_by_id(session_id: int) -> Session | None:
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sessions where session_id = ?", (session_id,))
        row = cursor.fetchone()
        return convert_session_row(row) if row else None

def save_new_session(session: Session) -> None:
    with get_connection() as connection:
        cursor = connection.cursor()
        if session.id == 0:
            cursor.execute(
                """
                INSERT INTO sessions (session_date, session_duration, subject_id)
                VALUES (?, ?, ?)
                """,
                (session.date, session.duration, session.subject_id),
            )
            session.id = cursor.lastrowid
        connection.commit()

def delete_session(session: Session) -> None:
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM sessions where session_id = ?",
            (session.id,)
        )
        connection.commit()
        
def update_session(session: Session) -> None:
    if session.id == 0:
        raise ValueError("Cannot update a session without an ID")
        
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE sessions
            set session_date = ?,
                session_duration = ?,
                subject_id = ?
            Where session_id = ?
            """,
            (
                session.date,
                session.duration,
                session.subject_id,
                session.id,
                
                ),
            )
        connection.commit()
        

def get_sessions_by_date(search_date: str) -> list[Session]:

    
    try:
        datetime.strptime(search_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM sessions WHERE session_date = ? ORDER BY session_id DESC",
            (search_date,)
        )
        rows = cursor.fetchall()
        return [convert_session_row(row) for row in rows]