#11
from builtins import open

try:
    file = open("log.txt", "r")

    error = 0
    warning = 0
    info = 0

    for line in file:
        if "ERROR" in line:
            error += 1
        if "WARNING" in line:
            warning += 1
        if "INFO" in line:
            info += 1

    file.close()

    print("Errors:", error)
    print("Warnings:", warning)
    print("Info:", info)

except FileNotFoundError:
    print("Log file not found")

#12

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll number: ")

        with open("students.txt", "a") as f:
            f.write(roll + "," + name + "\n")

        print("Student added!")

    elif choice == "2":
        try:
            with open("students.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No student records found")

    elif choice == "3":
        roll = input("Enter roll number to search: ")
        found = False

        try:
            with open("students.txt", "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if data[0] == roll:
                        print("Name:", data[1])
                        found = True
                        break
            if not found:
                print("Student not found")
        except FileNotFoundError:
            print("No student records found")

    elif choice == "4":
        roll = input("Enter roll number to update: ")
        found = False

        try:
            with open("students.txt", "r") as f:
                lines = f.readlines()

            with open("students.txt", "w") as f:
                for line in lines:
                    data = line.strip().split(",")
                    if data[0] == roll:
                        name = input("Enter new name: ")
                        f.write(roll + "," + name + "\n")
                        found = True
                    else:
                        f.write(line)

            if found:
                print("Student updated!")
            else:
                print("Student not found")

        except FileNotFoundError:
            print("No student records found")

    elif choice == "5":
        break

    else:
        print("Invalid choice")

#13

import csv

try:
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)

        print("Employee Payroll Summary")

        for row in reader:
            name = row["Name"]
            basic = float(row["Basic"])
            allowance = float(row["Allowance"])

            gross = basic + allowance
            deduction = basic * 0.10
            net = gross - deduction

            print("\nName:", name)
            print("Gross Salary:", gross)
            print("Deduction:", deduction)
            print("Net Salary:", net)

except FileNotFoundError:
    print("CSV file not found")
