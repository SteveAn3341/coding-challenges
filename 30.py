# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false


def xo(s):
    x = "x"
    o = "o"
    count_x = 0 
    count_o = 0
    s = s.lower()  # Convert the string to lower case to make the function case-insensitive
    for i in s:
        if i == x:
            count_x += 1
        elif i == o:
            count_o += 1
    
    # Return True if the counts are equal, else return False
    return count_x == count_o