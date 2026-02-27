def count_subarray(l,k):
    s,e = 0,1
    n = len(l)
    ans = 0
    while e <= n:
        list_sum = sum(l[s:e])
        print(l[s:e])
        if list_sum == k:
            ans += 1
            e += 1
        elif list_sum > k:
            s += 1
        else:
            e += 1
        
    return ans

l = [3,1,2,4]
k = 6
print(count_subarray(l,k))