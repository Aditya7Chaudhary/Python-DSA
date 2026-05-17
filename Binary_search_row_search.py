def row_most_ones(l):
    x = len(l)
    y = len(l[0])
    ans = [x,y]

    for i in range(x):
        s = 0
        e = y-1
        
        while s < e:
            m = s + (e-s)//2
            if l[i][m] == 1:
                e = m
            else:
                s = m+1

        if l[i][s] == 1:
            if ans[1] > s:
                ans = [i,s]
            elif ans[1] == s:
                ans = [min(ans[0],i),s]

    if ans[1] == y:
        return -1
    else:
        return ans[0]

l = [[0,0,1],[0,1,1],[0,0,0]]
print(row_most_ones(l))