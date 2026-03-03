def min_rotated_sorted_array(l):
    s = 0
    e = len(l)-1
    min_num = l[e]

    while s <= e:
        m = s + (e-s)//2
        
        if l[m] >= l[s]:
            if min_num > l[s]:
                min_num = l[s]
            s = m+1
        else:
            if min_num > l[m]:
                min_num = l[m]
            e = m-1

    return min_num

nums = [5,1,2,3,4]
print(min_rotated_sorted_array(nums))
        