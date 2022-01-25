# You're developing a new programming language with some unusual features for strings! Among these is a method that returns the longest palindrome that can be formed with the characters of a given string.

# Given a string s, your task is to find this longest possible palindrome. You may use any number of the characters from s, and arrange them in any order (so long as it results in a palindrome).

# If there are multiple longest palindromes that can be formed, return the one among them that's lexicographically smallest.

# Example

# For s = "aaabb", the output should be maximalPalindrome(s) = "ababa".

# There are two possible palindromes of length 5 that can be obtained ("ababa" and "baaab"), but "ababa" is lexicographically smaller, thus it is the answer.

# For s = "aaabbbcc", the output should be maximalPalindrome(s) = "abcacba".

# It's not possible to form a palindrome of length 8, but from several palindromes of length 7, "abcacba" is the lexicographically smallest, thus it is the answer.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string s

# The given string.

# Guaranteed constraints:
# 1 ≤ s.length ≤ 105.

# [output] string

# The lexicographically smallest palindrome with maximal length that can be built from the given string s.
def maximalPalindrome(s):
    store = [0] * 26
    
    for c in s:
        store[ord(c) - ord('a')] += 1
    
    front = ""
    back = ""
    middle = ""
    
    for i, n in enumerate(store):
        times = n // 2
        if n > 0:
            front = front + chr(i + ord('a')) * times
            back = chr(i + ord('a')) * times + back
        
        if middle == "" and n % 2 != 0:
            middle = chr(i + ord('a'))

    return front + middle + back