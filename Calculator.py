# Function to perform basic arithmetic operations
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Main function to get user input and display the result
def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")
        
        result = calculate(num1, num2, operation)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the main function
if __name__ == "__main__":
    main()
