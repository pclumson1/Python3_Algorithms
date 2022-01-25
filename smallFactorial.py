# -------------------------------------------------------------------
# Finds the smallest factorial result relative to the given integer n
#
# Problem #25
#

def leastFactorial(n):

    factorial = 1
    result = 1

    while result < n:

        factorial += 1
        result *= factorial

    return result

# -------------------------------------------------------------------
# Finds the smallest factorial result relative to the given integer n
#
# Problem #26
#

def countSumOfTwoRepresentations2(n, l, r):

    count = 0

    for index in range(l, r + 1):

        if(index <= (n - index) and (n - index) <= r): count += 1

    return count
