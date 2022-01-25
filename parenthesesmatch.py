#parenthesesmatch

def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0


#######################################################################

def isMatchingParenteses(s):
    stack = []

    opening = set('([{') 

    closing = set(')]}') 

    pair = {')':'(', ']':'[', '}':'{'} 

    for i in s :
        if i in opening :
            stack.append(i)

        if i in closing :
            if not stack :
                return False 

            elif stack.pop() != pair[i] :
                return False 
            else :
                continue 

        if not stack:
            return True 
        else:
            return False 



