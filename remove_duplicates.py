# Brute-force Solution 

def remove_duplicates(l):
    lu = [l[0]]
    for i in range(1,len(l)):
        if l[i] != l[i-1]:
            lu.append(l[i])
    return lu

# Optimized Solution 

def opt_remove_duplicates(l):
    if not l:
        return []

    j = 0
    for i in range(1, len(l)):
        if l[i] != l[j]:
            j += 1
            l[j] = l[i]
            
    return l[:j+1]


l = [1,2,2,3,3,5,6,7,7]
print(remove_duplicates(l))
print(opt_remove_duplicates(l))