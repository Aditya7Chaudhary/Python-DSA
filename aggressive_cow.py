def aggressive_cow(l,k):
    l.sort()
    n = len(l)

    s = 1
    e = (max(l)-min(l))//(k-1)
    ans = 1

    while s <= e:
        m = s + (e-s)//2

        cow_stored = 1
        prev_cow = l[0]
        for i in range(1,n):
            if l[i] - prev_cow >= m:
                cow_stored += 1
                prev_cow = l[i]
            
        if cow_stored >= k:
            ans = m
            s = m+1
        elif cow_stored < k:
            e = m-1

    return ans

l = [0,3,4,7,10,9]
k = 4
print(aggressive_cow(l,k))