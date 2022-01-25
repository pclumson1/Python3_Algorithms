# Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. Return the array of these digits in ascending order.

# Example

# For a = [25, 2, 3, 57, 38, 41], the output should be mostFrequentDigits(a) = [2, 3, 5].

# Here are the number of times each digit appears in the array:

# 0 -> 0
# 1 -> 1
# 2 -> 2
# 3 -> 2
# 4 -> 1
# 5 -> 2
# 6 -> 0
# 7 -> 1
# 8 -> 1
# The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].

def mostFrequentDigits(a):
    str1 = "".join(str(n) for n in a)
    
    store = {}
    max_count = 0
    ans = []
    
    for c in str1:
        if c in store:
            store[c] += 1
        else:
            store[c] = 1
        
        if store[c] > max_count:
            max_count = store[c]
            ans = [int(c)]
        elif store[c] == max_count:
            ans.append(int(c))
        
    return sorted(ans)