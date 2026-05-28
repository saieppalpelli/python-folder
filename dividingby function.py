def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The result of dividing {num1} by {num2} is: {result}")
    finally:
        print("Execution completed.")
divide_numbers()