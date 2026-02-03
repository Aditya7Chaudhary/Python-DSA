def longest_subarray(l,k):
    sum = 0
    f = 0
    ans = 0
    for i in range(len(l)):
        sum += l[i]
        if sum > k:
            sum -= l[f]
            f += 1
        elif sum == k:
            ans = i-f+1
    
    return ans

l = [-3, 2, 1]
k = 6

print(longest_subarray(l,k))
