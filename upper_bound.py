def upper_bound(l,k):
    s = 0
    e = len(l)-1
    min_index = -1

    while s <= e:
        m = s + (e-s)//2

        if l[m] > k:
            min_index = m
            e = m-1
        else:
            s = m+1
        
    return min_index
    
nums = [1,2,2,4]
target = 2
print(upper_bound(nums,target))

