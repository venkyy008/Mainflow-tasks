def count_words(sentence):
    words = sentence.split()  # Split the sentence into a list of words
    return len(words)  # Return the number of words

# Example usage:
sentence = "Count the number of words in a sentence."
print("Number of words:", count_words(sentence))
