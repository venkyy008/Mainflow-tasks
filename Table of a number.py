def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} × {i} = {n * i}")

# Example usage
nnn = int(input("Enter a number: "))
multiplication_table(nnn)