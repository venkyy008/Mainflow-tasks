def is_pythagorean_triplet(a, b, c):
    # Sort the numbers to ensure c is the largest
    a, b, c = sorted([a, b, c])
    
    # Check if a^2 + b^2 equals c^2
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

# Example usage
a = 3
b = 4
c = 5

if is_pythagorean_triplet(a, b, c):
    print(f"The numbers {a}, {b}, {c} form a Pythagorean triplet.")
else:
    p
