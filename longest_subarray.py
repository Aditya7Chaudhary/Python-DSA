def longest_subarray(l,k):
    sum = 0
    f = 0
    ans = 0
    i = 0
    while i < len(l):
        if sum > k:
            sum -= l[f]
            f += 1
        else:
            if i == len(l): break
            sum += l[i]
            i += 1
        if sum == k and ans < i-f:
            ans = i-f
    
    return ans

l = [10, 5, 2, 7, 1, 9]
k = 15

print(longest_subarray(l,k))
