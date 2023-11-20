def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = add(number1, number2)
    operation = "+"
elif choice == '2':
    result = subtract(number1, number2)
    operation = "-"
elif choice == '3':
    result = multiply(number1, number2)
    operation = "*"
elif choice == '4':
    result = divide(number1, number2)
    operation = "/"
else:
    print("Invalid input. Please enter a valid choice.")
    exit()

print(f"{number1} {operation} {number2} = {result}")
