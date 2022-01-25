# You are given three integers in the form of strings: firstnum, secondnum, and thirdnum. Your task is to check whether it is possible to erase at most one digit from firstnum, so that the resulting string contains at least one digit, has no leading zeros and the value of thirdnum is equal to the sum of the values of firstnum and secondnum.

# Return true if it's possible, otherwise return false.

# Note: All three strings are provided without leading zeros.

# Example

# For firstnum = "10534", secondnum = "67", and thirdnum = "1120", the output should be eraseOneDigit(firstnum, secondnum, thirdnum) = true.

# By erasing the 5th digit of firstnum, the result is 1053, and 1053 + 67 = 1120. So the answer is true.

# For firstnum = "10000", secondnum = "67", and thirdnum = "1120", the output should be eraseOneDigit(firstnum, secondnum, thirdnum) = false.

# The only possible modified values of firstnum would be 10000 (nothing was deleted), 0000 (first digit was deleted), and 1000 (any zero was deleted); none of which would produce the required sum, so the answer is false.

# For firstnum = "1067", secondnum = "33", and thirdnum = "100", the output should be eraseOneDigit(firstnum, secondnum, thirdnum) = false.

# We could delete the first digit of firstnum, resulting in 067 (and 67 + 33 = 100), but since in this case new firstnum value has a leading zero, it's considered invalid. So the answer is false.

# For firstnum = "153", secondnum = "153", and thirdnum = "306", the output should be eraseOneDigit(firstnum, secondnum, thirdnum) = true.

# Because 153 + 153 = 306, there's no need to delete a digit from firstnum, and the result is true.

def eraseOneDigit(firstnum, secondnum, thirdnum):
    for i in range(len(firstnum)):
        new = firstnum[:i] + firstnum[i+1:]
        if (
            int(new) + int(secondnum) == int(thirdnum) and
            len(new) == len(str(int(new)))
            ):
            return True
    
    if int(firstnum) + int(secondnum) == int(thirdnum):
        return True
    
    return False