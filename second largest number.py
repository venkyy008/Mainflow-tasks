def second_largest(nums):
    unique_nums = list(set(nums))  # Remove duplicates
    if len(unique_nums) < 2:
        return "No second largest number."
    unique_nums.sort(reverse=True)  # Sort in descending order
    return unique_nums[1]

# Example usage
nums = [10, 20, 4, 45, 99, 99]
print("Second largest number:", second_largest(nums))