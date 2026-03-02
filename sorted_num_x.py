def sorted_num_x(l,k):
    s = 0
    e = len(l)-1
    m = s + (e-s)//2

    while s <= e:
        m = s + (e-s)//2

        if l[m] == k:
            return m
        elif l[m] < k:
            s = m+1
        else:
            e = m-1
    
    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(sorted_num_x(nums,target))