def rec_bubble_sort(l,N):
    if N <= 0:
        return l
    for i in range(1,N):
        if l[i] < l[i-1]:
            l[i], l[i-1] = l[i-1], l[i]

    return rec_bubble_sort(l,N-1)

l = [5,4,3,2,1]
print(rec_bubble_sort(l,len(l)))