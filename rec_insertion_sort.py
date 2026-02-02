def rec_insertion_sort(l,N):
    if N <= 0:
        return
    
    rec_insertion_sort(l,N-1)

    for i in range(N-1,0,-1):
        if l[i] < l[i-1]:
            l[i], l[i-1] = l[i-1], l[i]

    return l
    
l = [5,4,2,4,3,1]
print(rec_insertion_sort(l,len(l)))