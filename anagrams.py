def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example usage
s1 = "listen"
s2 = "silent"

if are_anagrams(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")