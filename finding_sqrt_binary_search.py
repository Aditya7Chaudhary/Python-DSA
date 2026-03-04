def finding_sqrt(n):
    s = 1
    e = n//2 + 1

    if n == 1:
        return 1
    
    while s < e:
        m = s + (e-s)//2

        if m**2 <= n < (m+1)**2:
            return m
        elif m**2 > n:
            e = m
        else:
            s = m+1
    
n = 121
print(finding_sqrt(n))
