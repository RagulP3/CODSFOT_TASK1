def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        
        if choice == 5:
            break
        
        if choice in [1, 2, 3, 4]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue
            
            if choice == 1:
                result = add(num1, num2)
                operation = "Addition"
            elif choice == 2:
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == 3:
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == 4:
                result = divide(num1, num2)
                operation = "Division"
            
            print(f"{operation} of {num1} and {num2} is: {result}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
