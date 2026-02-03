def union_sorted_array(l1,l2):
    i = 0
    j = 0
    l = []
    while i < len(l1) and j < len(l2):
        if l1[i] not in l and l2[j] not in l:
            if l1[i] <= l2[j]:
                l.append(l1[i])
                i += 1
            else:
                l.append(l2[j])
                j += 1
        elif l1[i] in l and l2[j] in l:
            i += 1
            j += 1
        elif l2[j] in l:
            j += 1
        else:
            i += 1
    
    if i >= len(l1):
        for a in range(j,len(l2)):
            if l2[a] not in l:
                l.append(l2[a])
    elif j >= len(l2):
        for a in range(i,len(l1)):
            if l1[a] not in l:
                l.append(l1[a])

    return l

l1 = [1,3,5,6,6,7]
l2 = [2,4,5,7,8,8,9]

print(union_sorted_array(l1,l2))