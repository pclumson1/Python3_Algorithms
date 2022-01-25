

# function to check if two strings are
# anagram or not
def anagram(s1, s2):
     
    # the sorted strings are checked
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
       


#commonCharacterCount
def commonCharacterCount(s1, s2):
    #find intersection(common elements) and put them into a list
    s = list(set(s1))
    sum1 = 0
    for i in s:
        #count the no.of occurances of each char in s1 and s2 and take the min to avoid duplication
        sum1+=min(s1.count(i),s2.count(i)) 
    return sum1 


def isBananagram(s1, s2):

    # if((commonCharacterCount(s1, s2)) and ( sorted(s1)== sorted(s2))):

    if((commonCharacterCount(s1, s2)) and anagram(s1, s2)):

        print("The string are Bannagrams") 

    else:
        print("The string are not bananagrams")