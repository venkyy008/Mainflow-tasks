def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

# Example usage
lst = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
print("Duplicate elements:", find_duplicates(lst))