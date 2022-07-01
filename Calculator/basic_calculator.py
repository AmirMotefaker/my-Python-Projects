# Code by @AmirMotefaker

# Basic Calculator


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


# Output:
# Select operation.
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Divide
# Enter choice(1/2/3/4): 1
# Enter first number: 1
# Enter second number: 2
# 1.0 + 2.0 = 3.0
# Let's do next calculation? (yes/no): yes
# Enter choice(1/2/3/4): 2
# Enter first number: 2
# Enter second number: 1
# 2.0 - 1.0 = 1.0
# Let's do next calculation? (yes/no): n
# Enter choice(1/2/3/4): 0
# Invalid Input
# Enter choice(1/2/3/4): 65
# Invalid Input
# Enter choice(1/2/3/4): 4
# Enter first number: 2
# Enter second number: 1
# 2.0 / 1.0 = 2.0
# Let's do next calculation? (yes/no): no   
