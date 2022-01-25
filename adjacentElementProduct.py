# AdjacentElementProduct
def adjacentElementsProduct(inputArray):
    maxi = -1000
    ans = [0]*len(inputArray)
    for i in range(len(inputArray)-1):
        ans[i] = inputArray[i] * inputArray[i+1]
        if ans[i] > maxi:
            maxi = ans[i]
    return maxi