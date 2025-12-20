import sqlite3
from model.session import Session
from model.subject import Subject



def initialize_database(connection: sqlite3.Connection) -> None:
    cursor = connection.cursor()
    cursor.execute("""    
          CREATE TABLE "sessions" (
	"session_id"	INTEGER NOT NULL UNIQUE,
	"session_date"	TEXT NOT NULL,
	"session_duration"	TEXT NOT NULL,
	"subject_id"	INTEGER NOT NULL,
	PRIMARY KEY("session_id" AUTOINCREMENT),
	FOREIGN KEY("subject_id") REFERENCES ""
);
          """)
    cursor.execute("""
          CREATE TABLE "subjects" (
	"subject_id"	INTEGER NOT NULL UNIQUE,
	"subject_name"	TEXT NOT NULL,
	"subject_lector"	TEXT NOT NULL,
	"subject_study_points"	INTEGER,
	PRIMARY KEY("subject_id" AUTOINCREMENT)
);
          """)
    connection.commit()
    connection.close()
    
   