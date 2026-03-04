def koko_eating_bananas(piles,h):
    n = len(piles)
    a = h//n
    max_banana = max(piles)
    total_banana = sum(piles)

    e = max(max_banana//a, total_banana//h)
    s = min(max_banana//a, total_banana//h)
    while s < e:
        m = s + (e-s)//2

        time = 0
        for i in range(len(piles)):
            time_i = piles[i]//m 
            if piles[i]%m == 0:
                time += time_i
            else:
                time += time_i + 1
        
        if time == h:
            return m
        elif time < h:
            e = m-1
        else:
            s = m+1

piles = [3,6,7,11]
h = 8
print(koko_eating_bananas(piles,h))