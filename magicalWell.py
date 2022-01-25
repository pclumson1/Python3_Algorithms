# --------------------------------------------------------
# Calculates the amount of money given by the magical well
# when casting a marble
#
# Problem #27

def magicalWell(a, b, n):
    
    salary = 0
    
    while n > 0:
        
        salary += a*b
        a += 1
        b += 1
        
        n -= 1
        
    return salary   