def leaders_array(l):
    n = len(l)
    check = l[n-1]
    ans = [check]
    for i in range(-2,-n-1,-1):
        if l[i] > check:
            ans.insert(0,l[i])
            check = l[i]

    return ans

l = [10, 22, 12, 3, 0, 6]
print(leaders_array(l))