def finding_Nth_root(k,n):
    s = 1
    e = k//n + 1

    if k == 1:
        return 1
    
    while s < e:
        m = s + (e-s)//2

        if m**n <= k < (m+1)**n:
            return m
        elif m**n > k:
            e = m
        else:
            s = m+1
    
k = 16
n = 4
print(finding_Nth_root(k,n))
