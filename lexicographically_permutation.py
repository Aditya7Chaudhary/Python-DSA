# 1 2 5 4 1
# 1 4 5 2 1
# 1 4 1 2 5

# 5 4 3 2 1
# 1 2 3 4 5


def lexicographically_permutation(l):
    s = 0
    e = len(l)-1
    for i in range(len(l)-2,-1,-1):
        if l[i+1] > l[i]:
            s = i
            break
    for i in range(s+1,len(l)):
        if l[s] > l[i]:
            l[s],l[i-1] = l[i-1],l[s]
            s += 1
            break
    
    while s < e:
        l[s],l[e] = l[e],l[s]
        s += 1
        e -= 1
    
    return l

l = [1, 3, 5, 4, 1]
print(lexicographically_permutation(l))
    
    