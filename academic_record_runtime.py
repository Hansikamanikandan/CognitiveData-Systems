students = (
    (101, "Arun", 75),
    (102, "Bala", 35),
    (103, "Cathy", 90),
    (104, "Divya", 60)
)

print("\nAll Students:")
for s in students:
    print(s)

sid = int(input("\nEnter Student ID to search: "))
for s in students:
    if s[0] == sid:
        print("Student Found:", s)

top = max(students, key=lambda x: x[2])
print("\nTop Scorer:", top)

print("\nStudents scoring < 40:")
for s in students:
    if s[2] < 40:
        print(s)

avg = sum(s[2] for s in students) / len(students)
print("\nAverage Marks:", avg)
