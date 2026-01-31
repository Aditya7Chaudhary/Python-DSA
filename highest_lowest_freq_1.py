def highest_lowest_freq(l,k):
    d = {}
    l.sort()
    for i in l:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    
    return max(d), min(d)

l = [1,2,4]
k = 5
print(highest_lowest_freq(l,k))