def allocating_min_pages(l,k):
    s = max(l)
    e = sum(l)
    ans = -1

    while s <= e:
        m = s + (e-s)//2

        students_allocated = 0
        max_pages = 0
        pages_allocated = 0
        for i in l:
            pages_allocated += i
            
            if pages_allocated > m:
                students_allocated += 1
                pages_allocated = i
            max_pages = max(max_pages,pages_allocated)
                
        if pages_allocated > 0:
            students_allocated += 1

        if students_allocated <= k:
            e = m-1
            ans = max_pages
        else:
            s = m+1
        
    return ans

l = [10, 20, 40]
k = 2
print(allocating_min_pages(l, k)) 