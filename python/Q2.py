students = {}

print("Student Grades Program")

# Add a student
name = input("Enter student name: ").title()
grade = int(input("Enter grade: "))

students[name] = grade

print("\nStudent added successfully")

# Update grade
update = input("Do you want to update grade? (yes/no): ").lower()

if update == "yes":

    update_name = input("Enter student name: ").title()

    if update_name in students:

        grade = int(input("Enter new grade: "))
        students[update_name] = grade

        print("Grade updated!")

    else:
        print("Student not found")

elif update == "no":

    add_new_student = input(
        "Do you want to add a new student? (yes/no): "
    ).lower()

    if add_new_student == "yes":

        newname = input("Enter student name: ").title()
        newgrade = int(input("Enter grade: "))

        students[newname] = newgrade

        print("Student added successfully")

    else:
        print("No new student added")

else:
    print("Invalid input")

print("Student information:", students)