students = []

def add_student():
    student_id = input("Enter ID: ").strip()
    for s in students:
        if s["id"] == student_id:
            print("⚠️ Student with this ID already exists.")
            return
    name = input("Enter Name: ").strip()
    age = int(input("Enter Age: "))
    course = input("Enter Course: ").strip()
    marks = float(input("Enter Marks: "))
    students.append({
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    })
    print("✅ Student added successfully!")

def delete_student():
    student_id = input("Enter Student ID to delete: ").strip()
    global students
    updated = [s for s in students if s["id"] != student_id]
    if len(updated) == len(students):
        print("⚠️ Student not found.")
    else:
        students = updated
        print("🗑️ Student deleted successfully!")

def search_student():
    query = input("Enter ID or Name to search: ").strip().lower()
    results = [s for s in students if s["id"].lower() == query or s["name"].lower() == query]
    if results:
        for s in results:
            print(s)
    else:
        print("⚠️ No student found.")

def filter_students():
    print("Filter Options: ")
    print("1. By Course")
    print("2. By Minimum Marks")
    choice = input("Enter choice: ")
    if choice == "1":
        course = input("Enter course name: ").strip().lower()
        results = [s for s in students if s["course"].lower() == course]
    elif choice == "2":
        min_marks = float(input("Enter minimum marks: "))
        results = [s for s in students if s["marks"] >= min_marks]
    else:
        print("⚠️ Invalid choice.")
        return
    if results:
        for s in results:
            print(s)
    else:
        print("⚠️ No students match the criteria.")

def top_k_students():
    if not students:
        print("⚠️ No data available.")
        return
    k = int(input("Enter K value: "))
    top_students = sorted(students, key=lambda x: x["marks"], reverse=True)[:k]
    print(f"🏆 Top {k} Students:")
    for idx, s in enumerate(top_students, 1):
        print(f"{idx}. {s['name']} (Marks: {s['marks']})")

def menu():
    while True:
        print("\n==== Student Database ====")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. Filter Students")
        print("5. Top-K Students")
        print("6. Exit")
        print("==========================")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            filter_students()
        elif choice == "5":
            top_k_students()
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

menu()
