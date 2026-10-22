operator = input("Choose an operator (+, -, *, /): ")

try:
    x = int(input("What's x: "))
    y = int(input("What's y: "))
    if operator == "*":
        print(x * y)
    elif operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    elif operator == "/":
        if y !=0:
            print(x / y)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operator")
except ValueError:
    print("Invalid")
