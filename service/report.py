import csv
import openpyxl
from db.subject_dao import get_all_subjects
from db.session_dao import get_all_sessions

def generate_csv(filename: str):
    subjects = get_all_subjects()
    sessions = get_all_sessions()
    
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        writer.writerow(["Session ID", "Date", "Duration", "Subject Name"])
        
        for s in sessions:
            subj_name = next((sub.name for sub in subjects if sub.id == s.subject_id), "")
            writer.writerow([s.id, s.date, s.duration, subj_name])

def generate_excel(filename: str):
    
    subjects = get_all_subjects()
    sessions = get_all_sessions()
    
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sessions report"
    
    ws.append(["Session ID", "Date", "Duration", "Subject Name"])
    
    for s in sessions:
        subj_name = next((sub.name for sub in subjects if sub.id == s.subject_id), "")
        ws.append([s.id, s.date, s.duration, subj_name])
        
    wb.save(filename)