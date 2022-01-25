# You are given an array of non-negative integers numbers. You are allowed to choose any number from this array and swap any two digits in it. If after the swap operation the number contains leading zeros, they can be omitted and not considered (eg: 010 will be considered just 10).

# Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing.

# Example

# For numbers = [1, 5, 10, 20], the output should be makeIncreasing(numbers) = true.

# The initial array is already strictly increasing, so no actions are required.

# For numbers = [1, 3, 900, 10], the output should be makeIncreasing(numbers) = true.

# By choosing numbers[2] = 900 and swapping its first and third digits, the resulting number 009 is considered to be just 9. So the updated array will look like [1, 3, 9, 10], which is strictly increasing.

# For numbers = [13, 31, 30], the output should be makeIncreasing(numbers) = false.

# The initial array elements are not increasing.
# By swapping the digits of numbers[0] = 13, the array becomes [31, 31, 30] which is not strictly increasing;
# By swapping the digits of numbers[1] = 31, the array becomes [13, 13, 30] which is not strictly increasing;
# By swapping the digits of numbers[2] = 30, the array becomes [13, 31, 3] which is not strictly increasing;
# So, it's not possible to obtain a strictly increasing array, and the answer is false.
def compare(arr1, arr2):
    store = []
    
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            store.append(i)
    
    return store

def getOptions(str):
    store = []
    
    for i in range(len(str) - 1):
        store.append(int(str[i + 1:] + str[:i + 1]))
    
    return store

def check(i, arr):
    curr = str(arr[i])
    
    options = getOptions(curr)
    
    if i == 0:
        for v in options:
            if v < arr[i + 1]:
                return True
    elif i == len(arr) - 1:
        for v in options:
            if v > arr[i - 1]:
                return True
    else:
        for v in options:
            if v > arr[i - 1] and v < arr[i + 1]:
                return True
    
    return False

def makeIncreasing(numbers):
    b = sorted(numbers)
    
    store = compare(numbers, b)
    
    print(store)
    
    if len(store) > 2 and store[-1] - store[0] != len(store) - 1:
        return False
    if len(store) == 0:
        return True
        
    if check(store[0], numbers) or check(store[1], numbers):
        return True
    else:
        return False

