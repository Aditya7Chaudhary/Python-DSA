def count_subarray(l,k):
    s,e = 0,0
    n = len(l)
    ans = 0
    list_sum = l[s]
    while e < n:
        
        if list_sum > k:
            list_sum -= l[s]
            s += 1
            continue
        elif list_sum == k:
            ans += 1

        e += 1
        if e < n:
            list_sum += l[e]
        
    return ans

l = [3,1,2,4]
k = 6
print(count_subarray(l,k))