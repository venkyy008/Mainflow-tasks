def is_valid_sudoku(board):
    def is_valid_group(group):
        """ Helper function to check if a row, column, or 3x3 box contains duplicates. """
        nums = [num for num in group if num != "."]
        return len(nums) == len(set(nums))  # Check for duplicates
    
    # Check rows
    for row in board:
        if not is_valid_group(row):
            return False
    
    # Check columns
    for col in zip(*board):  # Transposes the board to get columns
        if not is_valid_group(col):
            return False
    
    # Check 3x3 sub-grids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_grid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_group(sub_grid):
                return False
    
    return True

# Example usage
sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print("Is the Sudoku board valid?", is_valid_sudoku(sudoku_board))