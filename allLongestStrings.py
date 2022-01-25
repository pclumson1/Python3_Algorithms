#allLongestStrings
def allLongestStrings(inputArray):
    arr_len = [len(i) for i in inputArray]
    long = max(arr_len)
    strings = []
    for i in inputArray[0:]:
        if len(i) == long:
            strings.append(i) # or else strings = strings + [i]
    return strings