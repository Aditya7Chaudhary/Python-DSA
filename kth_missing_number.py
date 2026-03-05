def kth_missing_number(nums,k):
    s = 0
    n = len(nums)
    e = n-1

    index = None

    while s <= e:
        m = s + (e-s)//2

        if nums[m] > k+m:
            e = m-1
        else:
            index = m
            s = m+1
    
    if index == None:
        return k
    else:
        return (k + index + 1)

nums = [1,2]
k = 1
print(kth_missing_number(nums,k))