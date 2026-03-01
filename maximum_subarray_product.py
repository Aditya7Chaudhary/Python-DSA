def maximum_subarray_product(nums):
    if not nums: return 0
    
    max_product = float('-inf')
    prefix = 1
    suffix = 1
    n = len(nums)
    
    for i in range(n):
        if prefix == 0: prefix = 1
        if suffix == 0: suffix = 1
        
        prefix *= nums[i]
        suffix *= nums[n - 1 - i]

        max_product = max(max_product, prefix, suffix)
        
    return max_product

nums = [1, 2, -3, 0, -4, -5, 0]
print(maximum_subarray_product(nums)) 