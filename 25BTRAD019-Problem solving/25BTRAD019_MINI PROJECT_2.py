# Student Grading Automation

print("====== STUDENT GRADING SYSTEM ======")

name = input("Enter student name: ")

m1 = float(input("Enter marks for Python: "))
m2 = float(input("Enter marks for Mathematics: "))
m3 = float(input("Enter marks for Physics: "))
m4 = float(input("Enter marks for Electronics: "))
m5 = float(input("Enter marks for English: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n========== RESULT ==========")
print("Student Name :", name)
print("Total Marks  :", total, "/ 500")
print("Average      :", round(average, 2))
print("Grade        :", grade)
print("============================")
