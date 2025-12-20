import pandas as pd
import csv
from data_access.subject_repo import get_all_subjects
from data_access.session_repo import get_all_sessions

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
    
    data = []
    for s in sessions:
        subj_name = next((sub.name for sub in subjects if sub.id == s.subject_id), "")
        data.append({
            "Session ID": s.id,
            "Date": s.date,
            "Duration": s.duration,
            "Subject Name": subj_name
        })
    
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)  