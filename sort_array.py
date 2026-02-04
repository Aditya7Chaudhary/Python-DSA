def sort_array(l):
    left = 0
    right = len(l)-1
    i = 0
    while i <= right:
        if l[i] == 0:
            l[left],l[i] = l[i],l[left]
            left += 1
            i += 1
        elif l[i] == 2:
            l[right],l[i] = l[i],l[right]
            right -= 1
        else:
            i += 1
    
    return l

l = [2,0,2,1,1,2]
print(sort_array(l))