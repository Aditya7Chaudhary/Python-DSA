def count_subarray_xor(nums,k):
    prefix = {}
    ans = []
    n = len(nums)
    xor = 0

    for i in range(n):    
        s = 0
        xor ^= nums[i]

        if k^xor in prefix:
            for j in prefix[k^xor]:
                s = j+1
                ans.append(nums[s:i+1])

        if xor == k:
            ans.append(nums[:i+1])
        
        if xor in prefix:
            prefix[xor].append(i)
        else:
            prefix[xor] = [i]
    
    return ans

nums = [4, 2, 2, 6, 4]
k = 6
print(count_subarray_xor(nums,k))