students = {}

def add_student():
    try:
        student_id = input("Enter Student ID: ").strip()
        if student_id in students:
            print("Error: Student ID already exists!")
            return
        name = input("Enter name: ").strip()
        age = int(input("Enter age: ").strip())
        course = input("Enter course: ").strip()
        gpa = float(input("Enter GPA: ").strip())
        students[student_id] = (name, age, course, gpa)
        print("Student added successfully!")
    except ValueError:
        print("Error: Invalid input! Age must be an integer and GPA must be a number.")

def view_students():
    if not students:
        print("No student records found!")
        return
    print("\nStudent List:")
    print("ID\tName\tAge\tCourse\t\tGPA")
    print("-" * 50)
    for sid, details in students.items():
        print(f"{sid}\t{details[0]}\t{details[1]}\t{details[2]}\t{details[3]}")

def search_student():
    student_id = input("Enter Student ID to search: ").strip()
    if student_id in students:
        details = students[student_id]
        print(f"\nStudent Found:\nID: {student_id}\nName: {details[0]}\nAge: {details[1]}\nCourse: {details[2]}\nGPA: {details[3]}")
    else:
        print("Error: Student not found!")

def update_student():
    student_id = input("Enter Student ID to update: ").strip()
    if student_id in students:
        name, age, course, gpa = students[student_id]
        print("Leave blank to keep current value.")
        new_name = input(f"Enter new Name ({name}): ").strip() or name
        new_age = input(f"Enter new Age ({age}): ").strip()
        new_course = input(f"Enter new Course ({course}): ").strip() or course
        new_gpa = input(f"Enter new GPA ({gpa}): ").strip()
        try:
            age = int(new_age) if new_age else age
            gpa = float(new_gpa) if new_gpa else gpa
        except ValueError:
            print("Error: Invalid input! Age must be an integer and GPA must be a number.")
            return
        students[student_id] = (new_name, age, new_course, gpa)
        print("Student details updated successfully!")
    else:
        print("Error: Student not found!")

def delete_student():
    student_id = input("Enter Student ID to delete: ").strip()
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Error: Student not found!")

def list_students_by_course():
    if not students:
        print("No student records found!")
        return
    courses = set(student[2] for student in students.values())
    for course in courses:
        print(f"\nCourse: {course}")
        print("ID\tName\tAge\tGPA")
        print("-" * 40)
        for sid, details in students.items():
            if details[2] == course:
                print(f"{sid}\t{details[0]}\t{details[1]}\t{details[3]}")

def average_gpa():
    if not students:
        print("No student records found!")
        return
    total_gpa = sum(student[3] for student in students.values())
    avg = total_gpa / len(students)
    print(f"\nAverage GPA: {avg:.2f}")

# Main Menu Loop
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. List Students by Course")
    print("7. Average GPA")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        list_students_by_course()
    elif choice == "7":
        average_gpa()
    elif choice == "8":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 8.")
