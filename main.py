from service.report import generate_csv, generate_excel
from model.subject import Subject
from model.session import Session
from data_access.subject_repo import (
    get_all_subjects, get_subject_by_id,
    save_new_subject, update_subject, delete_subject
)
from data_access.session_repo import  (
    get_all_sessions, get_session_by_id,
    save_new_session, update_session, delete_session
)

def print_menu():
    print("\n=== Study Planner Menu ===")
    print("=== Subjects ===")
    print("1. View all subjects")
    print("2. Add new subject")
    print("3. Update subject")
    print("4. Delete subject")
    print("5. Search subject on name")
    print("=== Sessions ===")
    print("5. View all sessions")
    print("6. Add new session")
    print("7. Update session")
    print("8. Delete session")
    print("=== Generate ===")
    print("9. Generate CSV report")
    print("10. Generate Excel report")
    print("0. Exit")

def main():
    print("Welcome to Study Planner!")
    while True:
        print_menu()
        choice = input("Choose one of the menu options: ").strip()

        if choice == "1":
            subjects = get_all_subjects()
            for s in subjects:
                print(f"subject: {s.id}: {s.name}, Lector: {s.lector}, Points: {s.study_points}")

        elif choice == "2":
            name = input("Subject name: ").strip()
            lector = input("Lector name: ").strip()
            points = int(input("Amount of study points: ").strip())
            subject = Subject(0, name, lector, points)
            save_new_subject(subject)
            print("New Subject added!")

        elif choice == "3":
            id_ = int(input("Enter subject ID to update: ").strip())
            subject = get_subject_by_id(id_)
            if not subject:
                print("Subject not found!")
                continue

            subject.name = input(f"New name ({subject.name}): ") or subject.name
            subject.lector = input(f"New lector ({subject.lector}): ") or subject.lector
            points_input = input(f"New points ({subject.study_points}): ")
            if points_input:
                subject.study_points = int(points_input)

            update_subject(subject)
            print("Subject updated!")

        elif choice == "4":
            id_ = int(input("Enter subject ID to delete: ").strip())
            subject = get_subject_by_id(id_)
            if not subject:
                print("Subject not found.")
                continue
            delete_subject(subject)
            print("Subject deleted!")
            
            
        elif choice == "5":
            search_name = input("Enter the name (or part of the name) of the subject to search: ").strip().lower()
            subjects = get_all_subjects()
            matched_subjects = [sub for sub in subjects if search_name in sub.name.lower()]
        
            if not matched_subjects:
                print("No subjects found with that name.")
            else:
                print(f"Found {len(matched_subjects)} subject(s):")
                for sub in matched_subjects:
                    print(f"ID: {sub.id} | Name: {sub.name}")

        elif choice == "6":
            sessions = get_all_sessions()
            for s in sessions:
                print(f"{s.id}: Date: {s.date}, Duration: {s.duration}, Subject ID: {s.subject_id}")


        elif choice == "7":
            date = input("Session date (YYYY-MM-DD): ").strip()
            duration = int(input("Session duration (minutes): ").strip())
            subject_id = int(input("Subject ID: ").strip())
            session = Session(0, date, duration, subject_id)
            save_new_session(session)
            print("Session added!")

        elif choice == "8":
            id_ = int(input("Enter session ID to update: ").strip())
            session = get_session_by_id(id_)
            if not session:
                print("Session not found")
                continue

            session.date = input(f"New date ({session.date}): ") or session.date
            duration_input = input(f"New duration ({session.duration}): ")
            if duration_input:
                session.duration = int(duration_input)
            subject_input = input(f"New subject ID ({session.subject_id}): ")
            if subject_input:
                session.subject_id = int(subject_input)

            update_session(session)
            print("Session updated!")

        elif choice == "9":
            id_ = int(input("Enter session ID to delete: ").strip())
            session = get_session_by_id(id_)
            if not session:
                print("Session not found.")
                continue
            delete_session(session)
            print("Session deleted!")

        elif choice == "10":
            filename = input("Enter CSV filename: ").strip()
            generate_csv(filename)
            print(f"CSV report created: {filename}")

        elif choice == "11":
            filename = input("Enter Excel filename: ").strip()
            generate_excel(filename)
            print(f"Excel report generated: {filename}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
