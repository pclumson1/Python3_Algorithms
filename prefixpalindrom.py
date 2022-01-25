# Use the helper function to avoid string mutation
def prefixPalindrome(s):
    def prefixPalindromeHelper(s, start, end):
        if start == end:
            return ''
        # start from end to find the longest palindromic prefix
        for e in range(end, start + 1, -1):
            if s[start:e] == s[start:e][::-1]:
                return prefixPalindromeHelper(s, e, end)
        return s[start:]
    return prefixPalindromeHelper(s, 0, len(s))