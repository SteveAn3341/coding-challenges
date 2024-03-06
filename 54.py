# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"

# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"
def to_camel_case(text):
    if not text:
        return ""
    # Split the text by both '-' and '_'
    words = text.replace("-", " ").replace("_", " ").split()
    # The first word is kept as is if original is lowercase; otherwise, capitalize it
    first_word = words[0] if text[0].islower() else words[0].capitalize()
    # Capitalize the first letter of the remaining words (if any)
    camel_case_str = first_word + ''.join(word.capitalize() for word in words[1:])
    return camel_case_str