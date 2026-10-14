import pymongo
import random
from faker import Faker
from datetime import datetime, timedelta

# Configuration 
# Connect to the Router (Port 27017)
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "learntrack"
NUM_STUDENTS = 50
NUM_COURSES = 5
NUM_LOGS = 2000

fake = Faker()
client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]

def clear_data():
    """Wipes old data so we start fresh."""
    db.students.drop()
    db.courses.drop()
    db.activity_logs.drop()
    print("[-] Old data cleared.")

def generate_students():
    students = []
    print(f"[+] Generating {NUM_STUDENTS} students...")
    for _ in range(NUM_STUDENTS):
        s = {
            "student_id": fake.uuid4(),
            "name": fake.name(),
            "email": fake.email(),
            "signup_date": fake.date_this_year().isoformat(),
            "region": random.choice(["North America", "Europe", "Asia", "Africa", "South America"])
        }
        students.append(s)
    db.students.insert_many(students)
    return students

def generate_courses():
    courses = []
    topics = ["Big Data", "Machine Learning", "Cloud Computing", "Python Basics", "DevOps"]
    print(f"[+] Generating {NUM_COURSES} courses...")
    for i, topic in enumerate(topics):
        c = {
            "course_id": f"C10{i}",
            "title": f"Intro to {topic}",
            "difficulty": random.choice(["Beginner", "Intermediate", "Advanced"]),
            "modules": random.randint(5, 12)
        }
        courses.append(c)
    db.courses.insert_many(courses)
    return courses

def generate_activity_logs(students, courses):
    logs = []
    print(f"[+] Generating {NUM_LOGS} activity logs (simulating traffic)...")
    
    actions = ["login", "video_watch", "quiz_attempt", "logout", "pdf_download"]
    
    for _ in range(NUM_LOGS):
        student = random.choice(students)
        course = random.choice(courses)
        
        log = {
            "timestamp": fake.date_time_between(start_date="-30d", end_date="now").isoformat(),
            "student_id": student["student_id"],
            "course_id": course["course_id"],
            "action": random.choice(actions),
            "duration_seconds": random.randint(10, 300) if random.random() > 0.5 else 0
        }
        logs.append(log)
    
    # Batch insert for speed
    db.activity_logs.insert_many(logs)

if __name__ == "__main__":
    try:
        clear_data()
        students = generate_students()
        courses = generate_courses()
        generate_activity_logs(students, courses)
        print(f"\n[SUCCESS] Generated: {NUM_STUDENTS} Students, {NUM_COURSES} Courses, {NUM_LOGS} Logs.")
    except Exception as e:
        print(f"\n[ERROR] Could not connect to MongoDB. Is Docker running? \nError: {e}")
