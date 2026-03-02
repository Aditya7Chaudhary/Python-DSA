def search_element_rotated_array(l,k):
    s = 0
    e = len(l)-1

    while s <= e:
        m = s + (e-s)//2

        if l[m] == k:
            return m
        
        if l[s] == l[m] == l[e]:
            s += 1
            e -= 1
            continue
        
        if l[m] < l[s]:
            if l[m] < k and k <= l[e]:
                s = m+1
            else:
                e = m-1
        else:
            if l[m] > k and k >= l[s]:
                e = m-1
            else:
                s = m+1
        
    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
k = 2
print(search_element_rotated_array(nums,k))