students = []
choice = ""
while choice != "8":
    print("\n--- Student Records Manager ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search student")
    print("4. Upadte student")
    print("5. Delete student")
    print("6. Class Topper")
    print("7. Class averge")
    print("8. Exit")
    choice = input("Enter your choice: ")

    # ADD STUDENT 
    if choice == "1":
        rollno = input("Enter roll number: ")
        found = False

        for student in students:
            if student["rollno"] == rollno:
                found = True
                break

        if found:
            print("Roll number already exists!")

        else:
            name = input("Enter student name: ")
            java = int(input("Enter Java marks: "))
            python = int(input("Enter Python marks: "))
            cpp = int(input("Enter C++ marks: "))

            student = {
                "rollno": rollno,
                "name": name,
                "java": java,
                "python": python,
                "cpp": cpp
            }

            students.append(student)
            print("Student added successfully!")

       # VIEW STUDENT
    elif choice == "2":
        if len(students) == 0:
            print("No student records found!")
        else:
            print("Roll No\tName\tJava\tPython\tC++")

            for student in students:
                print(
                    student["rollno"], "\t",
                    student["name"], "\t",
                    student["java"], "\t",
                    student["python"], "\t",
                    student["cpp"]
                )
       # SEARCH STUDENT         
    elif choice == "3":
        search = input("Enter roll number or name: ").lower()
        found = False

        for student in students:
            if search == student["rollno"] or search == student["name"].lower():
                print("Roll No:", student["rollno"])
                print("Name:", student["name"])
                print("Java:", student["java"])
                print("Python:", student["python"])
                print("C++:", student["cpp"])
                found = True
                break

        if not found:
            print("Student not found!") 
        # UPDATE STUDENT    
    elif choice == "4":
        rollno = input("Enter roll number to update: ")
        found = False

        for student in students:
            if student["rollno"] == rollno:
                student["java"] = int(input("Enter new Java marks: "))
                student["python"] = int(input("Enter new Python marks: "))
                student["cpp"] = int(input("Enter new C++ marks: "))
                print("Marks updated successfully!")
                found = True
                break

        if not found:
            print("Student not found!") 

        # DELETE STUDENT    
    elif choice == "5":
        rollno = input("Enter roll number to delete: ")
        found = False

        for student in students:
            if student["rollno"] == rollno:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found!")     

        # CLASS TOPPER
    elif choice == "6":
        if len(students) == 0:
            print("No student records found!")
        else:
            topper = students[0]

            for student in students:
                total = student["java"] + student["python"] + student["cpp"]
                topper_total = topper["java"] + topper["python"] + topper["cpp"]

                if total > topper_total:
                    topper = student

            print("Class Topper:", topper["name"])
            print("Roll Number:", topper["rollno"])
            print("Total Marks:", topper["java"] + topper["python"] + topper["cpp"]) 
         # CLASS AVERAGE 
    elif choice == "7":
        if len(students) == 0:
            print("No student records found!")
        else:
            total_marks = 0

            for student in students:
                total_marks += student["java"] + student["python"] + student["cpp"]

            average = total_marks / (len(students) * 3)

            print("Class Average:", average)    
         # EXIT
    elif choice == "8":
        print("Program closed!")

    else:
        print("Invalid choice! Please try again.")         