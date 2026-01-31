def count_frequency(l):
    d = {}
    for i in l:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    
    return d

l = [10,5,10,5,5,10]
print(count_frequency(l))