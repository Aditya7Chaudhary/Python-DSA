def longest_common_prefix(l):
    n = len(min(l))
    ans = ""
    me = len(l)

    s = 0
    e = n

    while s <= e:
        m = s + (e-s)//2
        curr = l[0][:m]
        
        for i in range(me):
            if l[i][:m] != curr:
                e = m-1
                break
        if e != m-1:
            s = m+1
            ans = curr
    
    return ans

l = ["flower", "flow", "wlight"]
print(longest_common_prefix(l))