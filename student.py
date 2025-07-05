class Student:
    def __init__(self, name, age, course, student_id=None):
        self.id = student_id
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"[{self.id}] {self.name}, {self.age} years - enrolled in {self.course}"