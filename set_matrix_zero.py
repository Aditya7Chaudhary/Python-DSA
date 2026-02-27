def set_matrix_zero(matrix):
    c,r = set(),set()
    n = len(matrix[0])

    for j in range(len(matrix)):
        for i in range(n):
            if matrix[j][i] == 0:
                r.add(i)
                c.add(j)
    
    for j in c:
        matrix[j] = [0]*n
    
    for j in range(len(matrix)):
        for i in r:
            matrix[j][i] = 0
    
    return matrix


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_matrix_zero(matrix))