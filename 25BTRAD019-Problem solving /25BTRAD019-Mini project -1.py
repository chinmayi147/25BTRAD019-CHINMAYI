# Mini Project: Unit Converter
print("===== UNIT CONVERTER =====")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))
value = float(input("Enter the value: "))

if choice == 1:
print("Miles =", value * 0.621371)

elif choice == 2:
print("Kilometers =", value * 1.60934)

elif choice == 3:
print("Fahrenheit =", (value * 9/5) + 32)

elif choice == 4:
print("Celsius =", (value - 32) * 5/9)

else:
print("Invalid choice")
