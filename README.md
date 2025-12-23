# Python Assignment
Adrian Jaron

## Goal
A small terminal-based application to manage study sessions and subjects.
Users can add, update, delete, and view study sessions and subjects. The application can also export reports in CSV or Excel format.

## Technology
Python 3.11+

SQLite (lightweight local database)

## Libraries
environs: to read configuration from a .env file

pandas: for exporting to Excel

Standard libraries: sqlite3, csv, datetime

## Functions

### Implemented

Show all subjects

Show all study sessions

Export study sessions to CSV or Excel

Add a subject

Update a subject

Delete a subject

Add a study session

Update a study session

Delete a study session

Search subjects per name

Search sessions per date

## Database name

create a file .env in the main folder.
You have to type in the .env file the following:
DATABASE=data/your_database.db


replace your_database with your own db name.

Make sure the database file exists. By default, it should be located at data/database.db. If it doesn’t exist, create it manually using SQLite:

mkdir -p data
sqlite3 data/database.db

## How to run

1. Clone repository or download my zip

2. Create Virtual env
python -m venv .venv

3. Install every required library
pip install -r requirements.txt

4. Execute the code
python -m main

## Structure of db

I have 2 tables sessions and subjects.

#### Subjects

    CREATE TABLE IF NOT EXISTS subjects (
        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT NOT NULL,
        subject_lector TEXT NOT NULL,
        subject_study_points INTEGER
    );
   

#### Sessions
   
    CREATE TABLE IF NOT EXISTS sessions (
        session_id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_date TEXT NOT NULL,
        session_duration INTEGER NOT NULL,
        subject_id INTEGER NOT NULL,
        FOREIGN KEY(subject_id) REFERENCES subjects(subject_id)
    );
 
