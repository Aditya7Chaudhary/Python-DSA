def floor_ceil_sorted_array(l,k):
    s = 0
    e = len(l)-1

    while s <= e:
        m = s + (e-s)//2

        if l[m] <= k:
            s = m+1
        else:
            e = m-1

    return l[e],l[s]

nums = [3, 4, 4,5, 7, 8, 10]
x = 4
print(floor_ceil_sorted_array(nums,x))