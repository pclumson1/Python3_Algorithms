# Given two strings s and t, both consisting of lowercase English letters and digits, your task is to calculate how many ways exactly one digit could be removed from one of the strings so that s is lexicographically smaller than t after the removal. Note that we are removing only a single instance of a single digit, rather than all instances (eg: removing 1 from the string a11b1c could result in a1b1c or a11bc, but not abc).

# Also note that digits are considered lexicographically smaller than letters.

# Example

# For s = "ab12c" and t = "1zz456", the output should be removeOneDigit(s, t) = 1.
def removeOneDigit(s, t):
    counter = 0
    
    for i, c in enumerate(s):
        if ord(c) < 97:
            c = list(s)
            c.pop(i)
            if "".join(c) < t:
                counter += 1
    
    for i, c in enumerate(t):
        if ord(c) < 97:
            c = list(t)
            c.pop(i)
            if "".join(c) > s:
                counter += 1
    
    return counter