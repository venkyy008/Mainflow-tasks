import heapq

def k_largest_elements(nums, k):
    return heapq.nlargest(k, nums)

# Example usage
nums = [3, 1, 5, 12, 2, 11, 7]
k = 3
print("K largest elements:", k_largest_elements(nums, k))