def rotate_90_degrees(matrix):
    c = len(matrix)

    for i in range(c//2):
        matrix[i],matrix[c-i-1] = matrix[c-i-1],matrix[i]

    for j in range(c):
        for i in range(j,c-j):
            if i == c-j-1:
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
            else:
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
                matrix[c-j-1][c-i-1],matrix[c-i-1][c-j-1] = matrix[c-i-1][c-j-1],matrix[c-j-1][c-i-1]

    return matrix

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
matrix2 = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
# Output = [[5, 4, 2, 0], [6, 5, 0, 1], [7, 0, 3, 1], [0, 5, 1, 2]]
print(rotate_90_degrees(matrix1))
print(rotate_90_degrees(matrix2))