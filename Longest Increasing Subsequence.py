def length_of_LIS(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # dp[i] stores the length of LIS ending at index i

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:  # Check increasing condition
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # The longest subsequence found

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print("Length of LIS:", length_of_LIS(nums))