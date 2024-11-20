# Basic Calculator Program

def calculator():
    print("Welcome to the Basic Calculator!")
    
    try:
        # Get user input for the two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Get user input for the operation
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Perform the calculation
        if operation == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == "/":
            if num2 == 0:  # Check for division by zero
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Invalid operation. Please use +, -, *, or /.")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the calculator
calculator()
