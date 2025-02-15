def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    fib = [0] * (n + 1)
    fib[1], fib[2] = 0, 1  # Base cases

    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Example usage
n = 10
print(f"The {n}-th Fibonacci number is: {fibonacci(n)}")