def insertion_sort(l):
    for i in range(1,len(l)):
        for j in range(i,0,-1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
    return l

# Time complexity is O(n^2)

l = [13,13,46,24,52,20,9]
print(insertion_sort(l))