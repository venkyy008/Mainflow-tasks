def longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Find the longest word
    longest = max(words, key=len)
    
    return longest

# Example usage
sentence = "Find the longest word in a given sentence"
print("The longest word is:", longest_word(sentence))