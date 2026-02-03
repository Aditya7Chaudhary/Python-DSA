def left_rotate(l):
    return l[1:]+[l[0]]

l = [1,2,3,4,5]
print(left_rotate(l))

nums = [1,2,3,4,5]
k = 2
nums = nums[k+1:] + nums[:k+1]
print(nums)