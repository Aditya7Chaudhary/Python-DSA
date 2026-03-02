def search_insert_number(l,k):
    s = 0
    e = len(l)-1

    while s <= e:
        m = s + (e-s)//2

        if l[m] == k:
            return m
        elif l[m] < k:
            s = m+1
        else:
            e = m-1
    
    l = l[:s] + [k] + l[s:]

    return l

nums = [1,2,4,7]
x = 6
print(search_insert_number(nums,x))