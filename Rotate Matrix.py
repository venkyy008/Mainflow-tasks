def rotate_matrix_90(matrix):
    # Transpose the matrix
    matrix = list(zip(*matrix))
    # Reverse each row
    return [list(row[::-1]) for row in matrix]

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated = rotate_matrix_90(matrix)
for row in rotated:
    print(row)