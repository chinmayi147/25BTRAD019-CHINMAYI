print("Hello world")

name = input("Enter your name : ")
print(name)

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = a+b
d = a-b
print("Sum of two numbers:", c)
print("Difference of numbers: ", d)


print("1. Addition\n" \
"2. Substraction\n" \
"3. multiplication\n" \
"4. Division\n"
"5. area of circle\n"
"6. area of rectangle\n"
"7. area of square\n")

Operations = int(input("Enter a number :"))

if Operations in(1, 2, 3, 4):
    a = int(input("Enter 1st number:"))
    b = int(input("Enter 2nd number:"))
    if Operations==1:
        print("Addition:",(a+b))
    if Operations==2:
        print("Substraction:",(a-b))
    if Operations==3:
        print("Multiplication:",(a*b))
    if Operations==4:
        print("Division:",(a/b))

elif Operations==5:
    r = float(input("Enter the raduis:"))
    print("area of circle:", 22/7*r**2)

elif Operations==7:
    s = float(input("Side of square:"))
    print("area of square:", s**2)

elif Operations==6:
    l = float(input("Enter the length :"))
    b = float(input("Enter the breadth:"))
    print("area of rectangle:", l*b)

else :
    print("Entered number is invalid")

