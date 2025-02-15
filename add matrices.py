def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return result

# Example usage
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = add_matrices(A, B)

# Displaying the result
for row in result:
    print(row)