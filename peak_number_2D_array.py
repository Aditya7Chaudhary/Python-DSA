def peak_number_2D_array(matrix):
    a = len(matrix)
    b = len(matrix[0])
    
    s = 0
    e = a-1

    while s <= e:
        temp = [-1,-1,-1]
        m = s + (e-s)//2
        for i in range(b):
            if matrix[m][i] > temp[0]:
                temp = [matrix[m][i],m,i]

        if m > 0 and temp[0] <= matrix[m-1][temp[2]]:   
            e = m-1
        elif m < a-1 and temp[0] <= matrix[m+1][temp[2]]:
            s = m+1
        else:
            return [temp[1],temp[2]]
        

matrix = [[5, 10, 8], [4, 25, 7], [3, 9, 6]]
print(peak_number_2D_array(matrix))