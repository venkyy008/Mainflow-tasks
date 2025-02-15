def find_missing_number(arr):
    n = len(arr)
    # Calculate the expected sum of numbers from 1 to n+1
    expected_sum = (n + 1) * (n + 2) // 2
    # Calculate the sum of elements in the array
    actual_sum = sum(arr)
    # The missing number is the difference
    return expected_sum - actual_sum

# Example usage
arr = [1, 2, 4, 5, 6]  # Missing number is 3
missing = find_missing_number(arr)
print("The missing number is:", missing)