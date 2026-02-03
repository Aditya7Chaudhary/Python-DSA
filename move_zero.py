def move_zero(l):
    j = 0
    for i in range(len(l)):
        if l[i] != 0:
            l[j], l[i] = l[i], l[j]
            j += 1
    
    return l

l = [1,0,2,3,0,0,5,0,7]
print(l)
print(move_zero(l))