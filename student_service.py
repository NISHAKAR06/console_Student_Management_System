from db_manager import DBManager
from student import Student

class StudentService:
    def __init__(self):
        self.db = DBManager()

    def add_student(self, student: Student):
        self.db.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                        (student.name, student.age, student.course))

    def get_all_students(self):
        rows = self.db.execute("SELECT * FROM students", fetch=True)
        return [Student(name=row[1], age=row[2], course=row[3], student_id=row[0]) for row in rows]

    def find_student(self, student_id):
        row = self.db.execute("SELECT * FROM students WHERE id = ?", (student_id,), fetchone=True)
        if row:
            return Student(name=row[1], age=row[2], course=row[3], student_id=row[0])
        return None

    def update_student(self, student: Student):
        self.db.execute("UPDATE students SET name = ?, age = ?, course = ? WHERE id = ?",
                        (student.name, student.age, student.course, student.id))

    def delete_student(self, student_id):
        self.db.execute("DELETE FROM students WHERE id = ?", (student_id,))
