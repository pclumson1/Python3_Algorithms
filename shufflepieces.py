

def shuffleThePieces(arr, pieces):
    arrstr = listToString(arr)
    for piece in pieces:
        piecestr = listToString(piece)
        if(piecestr in arrstr):
            result = True
            arrstr = removepart(arrstr, piecestr)
            continue
        else:
            result = False
            break
    return (len(arrstr) == 0)
    
def removepart(whole, part):
    return whole.replace(part, "", 1)
    
def listToString(s):  
    return ''.join(map(str, s)) 


#############################################

def test(arr, pieces):
    d = {}
    for k,v in enumerate(arr):
        d[v] = k

    for piece in pieces:
        if len(piece) > 1:
            for p in range(0, len(piece) - 1):
                if d[piece[p]] + 1 != d[piece[p+1]]: # eg. piece = [6,3] --> d[6] = 4, d[3] = 3, d[6] + 1 != d[3] --> return False
                    return False
    
    return True
