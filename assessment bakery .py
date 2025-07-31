def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Error: Please enter valid numeric values.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"Success! The result of {num1} divided by {num2} is {result}.")
    finally:
        print("Processing complete. Thank you!")

divide_numbers()

        