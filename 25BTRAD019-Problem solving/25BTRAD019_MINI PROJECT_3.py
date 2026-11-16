#attendance tracker

students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Attendance")
    print("3. Display Attendance")
    print("4. Check Shortage")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students[name] = []
        print("Student added!")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            status = input("Enter P for Present or A for Absent: ").upper()

            if status == "P" or status == "A":
                students[name].append(status)
                print("Attendance updated!")
            else:
                print("Invalid status")
        else:
            print("Student not found")

    elif choice == "3":
        print("\nName\t\tAttendance\tPercentage")

        for name, records in students.items():
            total = len(records)
            present = records.count("P")

            if total > 0:
                percentage = (present / total) * 100
            else:
                percentage = 0

            print(name, "\t\t", records, "\t", percentage, "%")

    elif choice == "4":
        limit = float(input("Enter attendance threshold: "))

        for name, records in students.items():
            total = len(records)

            if total > 0:
                percentage = records.count("P") / total * 100

                if percentage < limit:
                    print(name, "has low attendance:", percentage, "%")

    elif choice == "5":
        break

    else:
        print("Invalid choice")

#sale data analyzer

products = {}

while True:
    print("\n1. Add Product")
    print("2. Update Sales")
    print("3. Display Sales")
    print("4. Total Revenue")
    print("5. Highest Selling Product")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity sold: "))
        price = float(input("Enter price per item: "))

        products[name] = {
            "quantity": quantity,
            "price": price
        }

        print("Product added!")

    elif choice == "2":
        name = input("Enter product name: ")

        if name in products:
            quantity = int(input("Enter new quantity sold: "))
            products[name]["quantity"] = quantity
            print("Sales updated!")
        else:
            print("Product not found")

    elif choice == "3":
        print("\nProduct\tQuantity\tRevenue")

        for name, details in products.items():
            revenue = details["quantity"] * details["price"]
            print(name, "\t", details["quantity"], "\t\t", revenue)

    elif choice == "4":
        total = 0

        for details in products.values():
            total += details["quantity"] * details["price"]

        print("Total Revenue:", total)

    elif choice == "5":
        if products:
            highest = max(
                products,
                key=lambda name: products[name]["quantity"]
            )
            print("Highest Selling Product:", highest)
            print("Quantity Sold:", products[highest]["quantity"])
        else:
            print("No products available")

    elif choice == "6":
        break

    else:
        print("Invalid choice")
