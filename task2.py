# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

# Function to display the calculator menu
def display_menu():
    print("$$$$$$$$ CALCULATOR $$$$$$$")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("==========================")

# Main function to run the calculator
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            # Prompt user for input
            num1 = float(input("Enter the 1st number: "))
            num2 = float(input("Enter the 2nd number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            print("Faster Calculation & Accurate Answers.Thanks For Using. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
