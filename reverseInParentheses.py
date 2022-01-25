
# You are given a string s that consists of English letters, punctuation marks, whitespace characters and brackets. It is guaranteed that the brackets in s form a regular bracket sequence.

# Your task is to reverse the strings in each pair of matching parenthesis, starting from the innermost one.

# Example

# For string s = a(bc)de the output should be

# reverseParentheses(s) = "acbde".



def reverseInParentheses(s):
    stack = []
    for x in s:
        if x == ")":
            tmp = ""
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop() # pop the (
            for item in tmp:
                stack.append(item)
        else:
            stack.append(x)

    return "".join(stack) 



def reverseInParenthese(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"') 



def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
            print (s[:start])
        if s[i] == ")":
            end = i
            print (end)
            return reverseParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s 


def reverseParentheses(s):
    from collections import Counter
    for i in range(Counter(s)['(']):
        one = s.rsplit('(',1)
        two = one[1].split(')',1)
        s = one[0]+two[0].replace(two[0],two[0][::-1]+two[1])
        print(s)
    return s