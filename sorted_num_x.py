def sorted_num_x(l,k):
    s = 0
    e = len(l)-1
    m = s + (e-s)//2

    while s < e:
        if l[m] == k:
            return m
        elif l[m] < k:
            s = m
            m = s + (e-s)//2
        else:
            e = m
            m = s + (e-s)//2
    
    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(sorted_num_x(nums,target))