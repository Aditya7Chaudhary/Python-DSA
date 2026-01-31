def highest_lowest_freq(l,k):
    d = {}
    l.sort()

    s = 0
    e = len(l)-1
    m = s + (e-s)//2
    ans = 1

    while s < e:
        a = 0
        for i in range(m,0,-1):
            a += l[m]-l[i-1]
            if a > k:
                e = m
                m = s + (e-s)//2
                ans = max(ans,m-i+1)
        
                

    for i in l:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    
    return max(d), min(d)

l = [1,2,4]
k = 5
print(highest_lowest_freq(l,k))