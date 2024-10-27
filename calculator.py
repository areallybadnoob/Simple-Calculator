import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero error!"
    else:
        return x / y

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def inv_sin(x):
    return math.asin(x)

def inv_cos(x):
    return math.acos(x)

def inv_tan(x):
    return math.atan(x)

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def percentage(x, y):
    return (x / y) * 100

while True:
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Sin")
    print("6. Cos")
    print("7. Tan")
    print("8. Inverse Sin")
    print("9. Inverse Cos")
    print("10. Inverse Tan")
    print("11. Power")
    print("12. Square Root")
    print("13. Percentage")
    print("14. Exit")

    choice = input("Enter your choice (1-14): ")

    if choice == '1':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(add(num1, num2))
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choice == '2':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(subtract(num1, num2))
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choice == '3':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(multiply(num1, num2))
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choice == '4':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(divide(num1, num2))
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choice == '5':
        try:
            num = float(input("Enter angle in radians: "))
            print(sin(num))
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == '6':
        try:
            num = float(input("Enter angle in radians: "))
            print(cos(num))
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == '7':
        try:
            num = float(input("Enter angle in radians: "))
            print(tan(num))
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == '8':
        try:
            num = float(input("Enter angle in radians: "))
            print(inv_sin(num))
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == '9':
        try:
            num = float(input("Enter angle in radians: "))
            print(inv_cos(num))
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == '10':
        try:
            num = float(input("Enter angle in radians: "))
            print(inv_tan(num))
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == '11':
        try:
            num1 = float(input("Enter base: "))
            num2 = float(input("Enter exponent: "))
            print(power(num1, num2))
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choice == '12':
        try:
            num = float(input("Enter number: "))
            print(square_root(num))
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == '13':
        try:
            num1 = float(input("Enter percentage: "))
            num2 = float(input("Enter value: "))
            print(percentage(num1, num2))
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    elif choice == '14':
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 14.")