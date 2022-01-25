






#commonCharacterCount
def commonCharacterCount(s1, s2):
    #find intersection(common elements) and put them into a list
    s = list(set(s1))
    sum1 = 0
    for i in s:
        #count the no.of occurances of each char in s1 and s2 and take the min to avoid duplication
        sum1+=min(s1.count(i),s2.count(i)) 
    return sum1