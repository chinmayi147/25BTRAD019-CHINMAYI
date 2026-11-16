#14
class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance or invalid amount!")

    def check_balance(self):
        print("Current Balance: Rs.", self.balance)

    def display_details(self):
        print("\n--- Account Details ---")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance: Rs.", self.balance)


# Creating an object
name = input("Enter account holder name: ")
acc_no = input("Enter account number: ")

account = BankAccount(name, acc_no)

while True:
    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        account.display_details()

    elif choice == 5:
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Try again.")

#15

class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        print("\n--- Library Books ---")

        for book in self.books:
            status = "Available" if book.available else "Issued"

            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Status:", status)
            print("-------------------")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully!")
                else:
                    print("Book is already issued!")
                return

        print("Book not found!")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book returned successfully!")
                else:
                    print("Book was not issued!")
                return

        print("Book not found!")


# Creating library object
library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        book_id = int(input("Enter Book ID to issue: "))
        library.issue_book(book_id)

    elif choice == 4:
        book_id = int(input("Enter Book ID to return: "))
        library.return_book(book_id)

    elif choice == 5:
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Try again.")

#16

import random

while True:

    print("\n===== DICE SIMULATOR =====")

    n = int(input("Enter number of dice to roll: "))

    if n <= 0:
        print("Please enter a valid number!")
        continue

    print("\nRolling the dice...")

    for i in range(n):
        result = random.randint(1, 6)
        print("Dice", i + 1, ":", result)

    choice = input("\nRoll again? (yes/no): ").lower()

    if choice != "yes":
        print("Thank you for playing!")
        break

    
