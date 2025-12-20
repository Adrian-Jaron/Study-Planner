from environs import Env
import sqlite3
from datetime import date, datetime
from model.subject import Subject
from data_access.connection import get_connection

env = Env()
env.read_env()
DATABASE_NAME = env.str("DATABASE")

def convert_subject_row(row: tuple) -> Subject:
    return Subject(
        id=row[0],
        name=row[1],
        lector=row[2],
        study_points=row[3]
    )

def get_all_subjects() -> list[Subject]:
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM subjects order by subject_id DESC")
        rows = cursor.fetchall()
        return [convert_subject_row(row) for row in rows]


def get_subject_by_id(subject_id: int) -> Subject | None:
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM subjects WHERE subject_id = ?",
            (subject_id,)
        )
        row = cursor.fetchone()
        return convert_subject_row(row) if row else None
    
    
def save_new_subject(subject: Subject) -> None:
    with get_connection() as connection:
        cursor = connection.cursor()
        if subject.id == 0:
            cursor.execute(
                """
                INSERT INTO subjects ( subject_name, subject_lector,
                           subject_study_points) 
                VALUES (?,?,?)
                """, 
            (subject.name, subject.lector, subject.study_points),
            )
            subject.id = cursor.lastrowid
    connection.commit()
    
def delete_subject(subject: Subject) -> None:
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM subjects where subject_id = ?",
            (subject.id,)
        )
        connection.commit()
        
        
def update_subject(subject: Subject) -> None:
    if subject.id == 0:
        raise ValueError("Cannot update a subject without an ID")
        
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE subjects
                subject_name = ?,
                subject_lector = ?,
                subject_study_points = ?,
            Where subject_id = ?
            """,
            (
                subject.name,
                subject.lector,
                subject.study_points,
                ),
            )
        connection.commit()