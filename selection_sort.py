def selection_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i+1,len(l)):
            if l[min_index] > l[j]:
                min_index = j

        l[i],l[min_index] = l[min_index],l[i]
            
    return l

l = [13,13,46,24,52,20,9]
print(selection_sort(l))

# time complexity is O(n^2) only as min/max functions are a loop themselves.