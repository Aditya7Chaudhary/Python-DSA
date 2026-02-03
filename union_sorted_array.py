def union_sorted_array(l1,l2):
    i = 1
    j = 1
    if l1[0] < l2[0]:
        l = [l1[0],l2[0]]
    elif l2[0] < l1[0]:
        l = [l2[0],l1[0]]
    else:
        l = [l1[0]]

    while i < len(l1) and j < len(l2):
        if l1[i] != l[-1] and l2[j] != l[-1]:
            if l1[i] <= l2[j]:
                l.append(l1[i])
                i += 1
            else:
                l.append(l2[j])
                j += 1
        elif l1[i] == l[-1] and l2[j] == l[-1]:
            i += 1
            j += 1
        elif l2[j] == l[-1]:
            j += 1
        else:
            i += 1
    
    if i >= len(l1):
        for a in range(j,len(l2)):
            if l2[a] != l[-1]:
                l.append(l2[a])
    elif j >= len(l2):
        for a in range(i,len(l1)):
            if l1[a] != l[-1]:
                l.append(l1[a])

    return l

l1 = [1,3,5,6,6,7]
l2 = [2,4,5,7,8,8,9]

print(union_sorted_array(l1,l2))