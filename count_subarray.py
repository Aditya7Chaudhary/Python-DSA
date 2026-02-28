def count_subarray(l,k):
    s = 0
    n = len(l)
    ans = 0
    prefix_sum = {0:1}
    list_sum = 0

    for e in range(n):
        list_sum += l[e]

        remove_target = list_sum - k
        if remove_target in prefix_sum:
            ans += 1

        prefix_sum[list_sum] = prefix_sum.get(list_sum,0) + 1
        
    return ans

l = [3,1,-2,4]
k = 2
print(count_subarray(l,k))