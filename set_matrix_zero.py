def set_matrix_zero(matrix):
    n = len(matrix[0])
    f = 0
    if 0 in matrix[0]:
        f = 1

    for j in range(1,len(matrix)):
        r = 0
        for i in range(n):
            if matrix[j][i] == 0:
                matrix[0][i] = 0
                r = 1
        if r == 1:
            matrix[j] = [0]*n
        
    for i in range(n):
        if matrix[0][i] == 0:
            for j in range(1,len(matrix)):
                matrix[j][i] = 0
    
    if f == 1:
        matrix[0] = [0]*n
    
    return matrix


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_matrix_zero(matrix))