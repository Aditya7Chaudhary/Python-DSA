def floor_ceil_sorted_array(l,k):
    s = 0
    e = len(l)-1

    while s <= e:
        m = s + (e-s)//2

        if l[m] == k:
            return l[m],l[m]
        elif l[m] < k:
            s = m+1
        else:
            e = m-1

    floor_val = l[e] if e >= 0 else None
    ceil_val = l[s] if s < len(l) else None

    return floor_val,ceil_val

nums = [3, 4, 4, 5, 7, 8, 10]
x = 6
print(floor_ceil_sorted_array(nums,x))