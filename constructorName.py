# Suppose you are creating a new programming language. This language will support OOP, and to make it special, you want some features of it to differ from the standard.

# In some languages (such as C or Java), class constructor names are forced to have the same name as the class. Here you want to weaken this restriction, and to allow constructor names to be acceptable as long as they're close to the class name. We will consider two strings close if one can be obtained from the other, using the following operations:

# swap any two symbols in one of the strings,
# swap occurrences of any two existing symbols in one of the strings (for example, if your string contains both as and bs, you can change all as to bs and all the bs to as).
# Now you want to write a method that finds out whether the given methodName is considered close to the given className, by the definition above.

# Hint: One of the possible ways to solve the task might be the following. For both methodName and className build a map with the numbers of occurrences of each symbol. Then check whether the sets of the keys of both maps, containing symbols of the names, are equal. Since all occurrences of any two existing symbols can be freely swapped, you can, finally, check whether the multisets of the values of both maps are also equal.

# Example

# For className = "abbzccc" and methodName = "babzzcz", the output should be
# constructorNames(className, methodName) = true.

# One possible way to transform "abbzccc" to "babzzcz" is this:

# "abbzccc" (this string is className)
# "babzccc" (swap positions of the first two characters)
# "babczzz" (switch all c and z characters)
# "babzzcz" (swap positions of the characters at indices 3 and 5; this string is now methodName)
def constructorNames(className, methodName):
    c = {}
    m = {}
    
    for x in className:
        if x in c:
            c[x] += 1
        else:
            c[x] = 1
    
    for x in methodName:
        if x in m:
            m[x] += 1
        else:
            m[x] = 1
    
    c_list_k = [key for key in c.keys()]
    m_list_k = [key for key in m.keys()]
    
    if set(c_list_k) != set(m_list_k):
        return False
    
    c_list_v = [value for value in c.values()]
    m_list_v = [value for value in m.values()]
    
    if sorted(c_list_v) != sorted(m_list_v):
        return False
    
    return True