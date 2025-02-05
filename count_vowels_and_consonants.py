def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char in consonants)
    return vowel_count, consonant_count
text = "Hello World!"
vowels, consonants = count_vowels_consonants(text)
print(f"Vowels: {vowels}, Consonants: {consonants}")