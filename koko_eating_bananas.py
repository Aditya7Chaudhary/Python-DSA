def koko_eating_bananas(piles,h):
    n = len(piles)
    a = h//n
    max_banana = max(piles)
    total_banana = sum(piles)

    e = max(max_banana//a, total_banana//h)+1
    s = min(max_banana//a, total_banana//h)
    if s == 0:
        s = 1
    ans = max_banana

    while s <= e:
        m = s + (e-s)//2

        time = 0
        for i in range(len(piles)):
            time_i = piles[i]//m 
            if piles[i]%m == 0:
                time += time_i
            else:
                time += time_i + 1
        
        if time <= h:
            ans = min(ans,m)
            e = m-1
        else:
            s = m+1

    return ans

piles = [312884470]
h = 312884469
print(koko_eating_bananas(piles,h))