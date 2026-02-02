def quick_sort(l):    
    l_left = []
    l_right = []

    for i in range(1,len(l)):
        if l[0] >= l[i]:
            l_left.append(l[i])
        else:
            l_right.append(l[i])
    
    if l_left == l:
        return l
    if l_right == l:
        return l
    
    return quick_sort(l_left) + [l[0]] + quick_sort(l_right)

l = [4,1,2,5,2,3]
print(quick_sort(l))