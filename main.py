from student_service import StudentService
from student import Student

def menu():
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Find Student by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def main():
    service = StudentService()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            course = input("Course: ")
            service.add_student(Student(name, age, course))
            print("Student added.")

        elif choice == '2':
            students = service.get_all_students()
            for s in students:
                print(s)

        elif choice == '3':
            sid = int(input("Enter ID: "))
            s = service.find_student(sid)
            print(s if s else "Student not found.")

        elif choice == '4':
            sid = int(input("Enter ID to update: "))
            student = service.find_student(sid)
            if student:
                name = input(f"New name ({student.name}): ") or student.name
                age = input(f"New age ({student.age}): ") or student.age
                course = input(f"New course ({student.course}): ") or student.course
                service.update_student(Student(name, int(age), course, sid))
                print("Updated.")
            else:
                print("Not found.")

        elif choice == '5':
            sid = int(input("ID to delete: "))
            service.delete_student(sid)
            print("Deleted.")

        elif choice == '6':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
