import sqlite3

# Connect to DB
conn = sqlite3.connect("students.db")
cur = conn.cursor()

# Create table
cur.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    grade REAL
)""")

def add_student(name, grade):
    cur.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))
    conn.commit()

def view_students():
    cur.execute("SELECT * FROM students")
    return cur.fetchall()

# Example usage
add_student("Alice", 15.5)
add_student("Bob", 13.7)
print(view_students())
