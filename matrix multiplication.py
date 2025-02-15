def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if multiplication is possible
    if cols_A != rows_B:
        return "Matrix multiplication is not possible."

    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B (same value)
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example matrices
A = [[1, 2, 3], 
     [4, 5, 6]]

B = [[7, 8], 
     [9, 10], 
     [11, 12]]

# Multiply matrices
result = multiply_matrices(A, B)

# Display the result
if isinstance(result, str):
    print(result)
else:
    for row in result:
        print(row)