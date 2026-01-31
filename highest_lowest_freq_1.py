def highest_lowest_freq(l):
    d = {}
    for i in l:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    
    return max(d), min(d)

l = [10,5,10,3,5,10]
print(highest_lowest_freq(l))