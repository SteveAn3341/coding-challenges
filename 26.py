# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.







def highest_scoring_word(s):
    # Split the string into words
    words = s.split()
    # Initialize the highest score and the word with that score
    highest_score = 0
    highest_scoring_word = ""
    
    # Iterate through each word
    for word in words:
        # Calculate the score of the word
        score = sum(ord(char) - 96 for char in word) # ord('a') is 97, so subtract 96 to get 1 for 'a', etc.
        # Update the highest score and word if this word's score is higher
        if score > highest_score:
            highest_score = score
            highest_scoring_word = word
    
    return highest_scoring_word