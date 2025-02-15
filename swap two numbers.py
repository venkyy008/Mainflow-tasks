# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swapping without a third variable
a, b = b, a

# Output the swapped values
print("After swapping:")
print("First number:", a)
print("Second number:", b)