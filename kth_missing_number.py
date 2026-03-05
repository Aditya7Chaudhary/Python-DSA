def kth_missing_number(nums,k):
    s = 0
    n = len(nums)
    e = n-1

    index = None

    while s <= e:
        m = s + (e-s)//2

        if nums[m] > k:
            e = m-1
        else:
            index = m
            s = m+1
    
    if index == None:
        return k
    else:
        return (k + index + 1)

nums = [4,7,9,10]
k = 4
print(kth_missing_number(nums,k))