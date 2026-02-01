def bubble_sort(l):
    for i in range(len(l)):
        for j in range(1,len(l)-i):
            if l[j-1] > l[j]:
                l[j],l[j-1] = l[j-1],l[j] 
    return l

l = [13,13,24,46,52,20,9]
print(bubble_sort(l))