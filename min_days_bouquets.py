def min_days_bouquets(l,k,bouquets):
    s = min(l)
    e = max(l)
    n = len(l)
    ans = -1

    if bouquets * k > n:
        return ans

    while s <= e:
        m = s + (e-s)//2
        
        possible_bouquets = 0
        flowers = 0
        for i in range(n):
            if l[i] <= m:
                flowers += 1
            else:
                flowers = 0

            if flowers == k:
                possible_bouquets += 1
                flowers = 0
        
            if possible_bouquets == bouquets:
                break
        
        if possible_bouquets == bouquets:
            ans = m
            e = m-1
        else:
            s = m+1
        
    return ans

bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
print(min_days_bouquets(bloomDay,k,m))