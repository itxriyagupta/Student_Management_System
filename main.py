students = []

# FUNCTION TO ADD STUDENTS

def add_student():
    registration_num = input("Enter the registration number:")
    
    for student in students:
        if student["registration_num"] == registration_num:
            print("Registration number already exists!")
            return
    
    name = input("Enter name: ")
    course = input("Enter course:")
    
    try: 
        age = int(input("Enter age:"))
        semester = int(input("Enter the semester:"))
        marks = float(input("Enter the marks:"))
        
    except ValueError:
        print("Invalid input . Age and semester must be integers, and marks must be a number .")
        return
    
    student = {
        "registration_num" : registration_num,
        "name" : name,
        "age" : age,
        "course" : course,
        "semester" : semester,
        "marks" : marks,
        }
    students.append(student)
    
    print("student added successfully")
    
# FUNCTION TO VIEW STUDENT
    
def view_student():
    if len(students) == 0:
        print("NO STUDENTS FOUND")
        return
    print("\n ******ALL STUDENTS******")
    
    for student in students:
        print("***********************************")
        print("Registration Number:", student["registration_num"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Semester:", student["semester"])
        print("Marks:", student["marks"])
            

# FUNCTION TO SEARCH STUDENT

def search_student():
    registration_num = input("Enter registration number to search: ")
    
    found = False
    
    for student in students:
        if student["registration_num"] == registration_num:
            print("\n******STUDENT FOUND******")
            print("Registration Number:" , student["registration_num"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("semester:", student["semester"])
            print("Marks:", student["marks"])
            
            found = True
            break
        
    if not found:
        print("STUDENT NOT FOUND")


# FUNCTION TO UPDATE STUDENT

def update_student():
    registration_num = input("Enter registration number to update: ")
    
    for student in students:
        if student["registration_num"] == registration_num:
            
            print("\n STUDENT FOUND. Enter new details: ")
            
            student["name"] = input("Enter new name: ")
            student["course"] = input("Enter new course: ")
            
            try:
                
                 student["age"] = int(input("Enter new age: "))
                 student["semester"] = int(input("Enter new semester: "))
                 student["marks"] = float(input("Enter new marks: "))
            except ValueError:
                print("Invalid input. Student details were not updated. ")
                return
            
            print("STUDENT DETAILS UPDATED SUCCESSFULLY")
            return
        
    print("STUDENT NOT FOUND")
        
        
# FUNCTION TO DELETE STUDENT

def delete_student():
    registration_num = input("Enter registration number to delete student: ")
    
    for student in students:
        if student["registration_num"] == registration_num:
            students.remove(student)
            print("STUDENT DELETED SUCCESSFULLY")
            return
        
    print(" STUDENT NOT FOUND")    
        
        
# FUNCTIONS TO SORT STUDENT BY MARKS

def sort_student():
    if len(students) == 0:
        print("NO STUDENTS FOUND")
        return
    
    print("\n******SORT STUDENTS******")
    print("1. Sort by marks(High to low)")
    print("2. Sort by marks( low to high)")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        students.sort(key=lambda student: student["marks"], reverse=True)
        print("Students sorted by marks from high to low")
              
    elif choice == "2":
        students.sort(key=lambda student: student["marks"])
        print("Students sorted by marks from low to high")
        
        
    else:
        print("INVALID CHOICE")
        return
    
    view_student()

# FUNCTION TO SAVE STUDENTS TO A FILE 
    
def save_student():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(
                student["registration_num"] + "," +
                student["name"] + "," +
                str(student["age"]) + "," +
                student["course"] + "," +
                str(student["semester"]) + "," +
                str(student["marks"]) + "\n"
            )
            
    print("STUDENT DATA SAVED SUCCESSFULLY")   


# FUNCTION TO LOAD STUDENTS FROM FILE
 
 
def load_student():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                
                if len(data) == 6:
                
                   student = {
                      "registration_num": data[0],
                      "name": data[1],
                      "age": int(data[2]),
                      "course": data[3],
                      "semester": int(data[4]),
                      "marks": float(data[5])
                }    
                
                   students.append(student)
                
    except FileNotFoundError:
        pass            
    
# LOAD EXISTING STUDENT DATA
load_student()    
    
    
 # MAIN MENU   
while True:
    print("\n******STUDENT MANAGEMENT SYSTEM******")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Sort students")
    print("7. Save student data")
    print("8. Exit")

    
    choice = input("Enter your choice:")
    
    if choice == "1":
        add_student()
        
    elif choice == "2":
        view_student()
        
    elif choice == "3":
        search_student()
        
    elif choice == "4":
        update_student()
        
    elif choice == "5":
        delete_student()
        
        
    elif choice == "6":
        sort_student()
        
    elif choice == "7":
        save_student()
        
        
    elif choice == "8":    
        print("THANKYOU FOR USING STUDENT MANAGEMENT SYSTEM")
        break
    else:
        print("INVALID CHOICE, TRY AGAIN!")
        
    