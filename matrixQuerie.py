# You are given a matrix of integers matrix of size n × m and a list of queries queries. The given matrix is colored in black and white in a checkerboard style - the top left corner is colored white and any two side-neighboring cells have opposite colors.

# Each query is represented as a pair of indices (i, j). For each query, perform the following operations:

# Select the ith-smallest value among the black cells. In case of a tie, select the one with the lower row number. If there is still a tie, select the one with the lower column number;
# Select the jth-smallest white cell using the same process;
# Find the average value of these two cells;
# If the average value is a whole integer, replace both of the selected cells with the found average value;
# Otherwise, replace the cell of the greater value with the average rounded up to the nearest integer, and replace the cell of the smaller value with the average rounded down to the nearest integer.
# Your task is to return the resulting matrix after processing all the queries.


def solution(matrix, queries):
    black, white, checker = [], [], 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j % 2 == checker: white.append((matrix[i][j], i, j))
            else: black.append((matrix[i][j], i, j)) 
        if not checker: checker = 1 
        else: checker = 0 
    
    black.sort(); white.sort() 
    for i, j in queries:
        b, w = black.pop(i), white.pop(j) 
        bval, wval, bi, bj, wi, wj = b[0], w[0], b[1], b[2], w[1], w[2]
        avg = (bval + wval) / 2 
        if avg % 1 == 0:
            matrix[bi][bj] = matrix[wi][wj] = avg 
            white.append((avg, wi, wj)); black.append((avg, bi, bj)) 
        else:
            high, low = max(b, w), min(b, w) 
            if high[0] == bval: flag = True 
            else: flag = False 
            matrix[high[1]][high[2]], matrix[low[1]][low[2]] = int(avg) + 1, int(avg) 
            if flag: 
                black.append((int(avg) + 1, high[1], high[2]))
                white.append((int(avg), low[1], low[2]))
            else:
                black.append((int(avg), low[1], low[2]))
                white.append((int(avg) + 1, high[1], high[2]))
        white.sort(); black.sort() 
    return matrix 