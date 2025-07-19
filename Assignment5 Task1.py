student_marks = {'Alice':85}
student_name = input("Enter a student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks are: {student_marks[student_name]}")

else:
    print("Student not found.")