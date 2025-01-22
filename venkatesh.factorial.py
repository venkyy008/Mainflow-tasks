import math
def factorial_program():
    print("Factorial Calculation Program")
    try:
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = math.factorial(n)
            print(f"The factorial of {n} is: {result}")
    except ValueError:
        print("Invalid input! Please enter a non-negative integer.")
factorial_program()
