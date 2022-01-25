# Given an array of positive integers a, your task is to calculate the sum of every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation of the string representations of a[i] and a[j] respectively.

# Example

# For a = [10, 2], the output should be concatenationsSum(a) = 1344.

# a[0] ∘ a[0] = 10 ∘ 10 = 1010,
# a[0] ∘ a[1] = 10 ∘ 2 = 102,
# a[1] ∘ a[0] = 2 ∘ 10 = 210,
# a[1] ∘ a[1] = 2 ∘ 2 = 22.
# So the sum is equal to 1010 + 102 + 210 + 22 = 1344.

# For a = [8], the output should be concatenationsSum(a) = 88.

# There is only one number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88, so the answer is 88.

# For a = [1, 2, 3], the output should be concatenationsSum(a) = 198.

# a[0] ∘ a[0] = 1 ∘ 1 = 11,
# a[0] ∘ a[1] = 1 ∘ 2 = 12,
# a[0] ∘ a[2] = 1 ∘ 3 = 13,
# a[1] ∘ a[0] = 2 ∘ 1 = 21,
# a[1] ∘ a[1] = 2 ∘ 2 = 22,
# a[1] ∘ a[2] = 2 ∘ 3 = 23,
# a[2] ∘ a[0] = 3 ∘ 1 = 31,
# a[2] ∘ a[1] = 3 ∘ 2 = 32,
# a[2] ∘ a[2] = 3 ∘ 3 = 33.
# The total result is 11 + 12 + 13 + 21 + 22 + 23 + 31 + 32 + 33 = 198.


# ***************************************************************************** #
# Practice June 3
# ***************************************************************************** #

# 1
# You are given an array of integers a and two integers l and r. You task is to calculate a boolean array b, where b[i] = true if there exists an integer x, such that a[i] = (i + 1) * x and l ≤ x ≤ r. Otherwise, b[i] should be set to false.

# Example

# For a = [8, 5, 6, 16, 5], l = 1, and r = 3, the output should be boundedRatio(a, l, r) = [false, false, true, false, true].

# For a[0] = 8, we need to find a value of x such that 1 * x = 8, but the only value that would work is x = 8 which doesn't satisfy the boundaries 1 ≤ x ≤ 3, so b[0] = false.
# For a[1] = 5, we need to find a value of x such that 2 * x = 5, but there is no integer value that would satisfy this equation, so b[1] = false.
# For a[2] = 6, we can choose x = 2 because 3 * 2 = 6 and 1 ≤ 2 ≤ 3, so b[2] = true.
# For a[3] = 16, there is no an integer 1 ≤ x ≤ 3, such that 4 * x = 16, so b[3] = false.
# For a[4] = 5, we can choose x = 1 because 5 * 1 = 5 and 1 ≤ 1 ≤ 3, so b[4] = true.

def boundedRatio(a, l, r):
    b = []
    
    for i, v in enumerate(a):
        x = v / (i + 1)
        if int(x) == x and l <= x and x <= r:
            b.append(True)
        else:
            b.append(False)
    
    return b