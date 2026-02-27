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

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(rotate_90_degrees(matrix))