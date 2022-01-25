# You are implementing your own programming language and you've decided to add support for merging strings. A typical merge function would take two strings s1 and s2, and return the lexicographically smallest result that can be obtained by placing the symbols of s2 between the symbols of s1 in such a way that maintains the relative order of the characters in each string.

# For example, if s1 = "super" and s2 = "tower", the result should be merge(s1, s2) = "stouperwer".

# You'd like to make your language more unique, so for your merge function, instead of comparing the characters in the usual lexicographical order, you'll compare them based on how many times they occur in their respective initial strings (fewer occurrences means the character is considered smaller). If the number of occurrences are equal, then the characters should be compared in the usual lexicographical way. If both number of occurences and characters are equal, you should take the characters from the first string to the result. Note that occurrences in the initial strings are compared - they do not change over the merge process.

# Given two strings s1 and s2, return the result of the special merge function you are implementing.

# Example 

# For s1 = "dce" and s2 = "cccbd", the output should be
# mergeStrings(s1, s2) = "dcecccbd".
# All symbols from s1 goes first, because all of them have only 1 occurrence in s1 and c has 3 occurrences in s2.
def mergeStrings(s1, s2):

    s1_ref = {}
    s2_ref = {}
    
    for c in s1:
        if c in s1_ref:
            s1_ref[c] += 1
        else: 
            s1_ref[c] = 1
            
    for c in s2:
        if c in s2_ref:
            s2_ref[c] += 1
        else: 
            s2_ref[c] = 1
    
    output = ""
    n_s1 = 0
    n_s2 = 0
    
    for i in range(len(s1) + len(s2)):
        s1_c = s1_ref[s1[n_s1]]
        s2_c = s2_ref[s2[n_s2]]
        print(output)
        print(n_s1)
        
        if n_s1 > len(s1) - 1:
            output += s2[n_s2:]
            break
        
        if n_s2 > len(s2) - 1:
            output += s1[n_s1:]
            break
        
        if s1_c < s2_c:
            output += s1[n_s1]
            n_s1 += 1
        elif s2_c < s1_c:
            output += s2[n_s2]
            n_s2 += 1
        elif s1[n_s1] < s2[n_s2]:
            output += s1[n_s1]
            n_s1 += 1
        elif s2[n_s2] < s1[n_s1]:
            output += s2[n_s2]
            n_s2 += 1
        else:
            output += s1[n_s1]
            n_s1 += 1
    
    return output
