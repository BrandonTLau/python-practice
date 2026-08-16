def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 / num2

def get_number(prompt):
    """Repeatedly prompts user until a valid number is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    """Repeatedly prompts user until a valid math operator is entered."""
    valid_ops = ['+', '-', '*', '/']
    while True:
        op = input("Enter operation (+, -, *, /): ").strip()
        if op in valid_ops:
            return op
        print("Invalid operator. Please choose from +, -, *, or /.")

def main():
    print("Python Calculator")
    print("----------------------------")
    
    while True:
        # Get validated inputs
        num1 = get_number("Enter first number: ")
        operation = get_operation()
        num2 = get_number("Enter second number: ")
        
        # Perform calculation
        try:
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
                
            print(f"Result: {num1} {operation} {num2} = {result}\n")
            
        except ZeroDivisionError as e:
            print(f"Math Error: {e}\n")
            
        # Loop prompt: check if the user wants to continue
        while True:
            choice = input("Do you want to perform another calculation? (y/n): ").strip().lower()
            if choice in ['y', 'n']:
                break
            print("Invalid option. Please enter 'y' or 'n'.")
            
        if choice == 'n':
            print("Goodbye!")
            break
        print("-" * 28)

if __name__ == "__main__":
    main()
