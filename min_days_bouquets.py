def min_days_bouquets(l,k,bouquets):
    s = min(l)
    e = max(l)
    n = len(l)
    ans = -1

    while s <= e:
        m = s + (e-s)//2
        
        i = 0
        possible_bouquets = 0
        while i <= n-k:
            if max(l[i:i+k]) >= m:
                possible_bouquets += 1
                i += k
            else:
                i += 1
        
        if possible_bouquets >= bouquets:
            ans = m
            s = m+1
        else:
            e = m-1
        
    return ans

bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(min_days_bouquets(bloomDay,k,m))