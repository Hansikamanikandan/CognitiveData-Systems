n = int(input("Enter number of students: "))
students = {}

for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter mark: "))
    students[name] = mark

search = input("Enter student name to search: ")

if search in students:
    print("Marks:", students[search])
else:
    print("Student not found")
