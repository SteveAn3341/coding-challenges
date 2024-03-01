# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"


def spin_words(sentence):
    empty_arr = []
    new_arr = sentence.split(" ")
    for i in new_arr:
        if len(i) < 5:
            empty_arr.append(i)
        elif len(i) >= 5:
            i = i[::-1]
            empty_arr.append(i)
                
    final_str =" ".join(empty_arr)
    return final_str