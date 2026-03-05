def smallest_divisor_threshold_array(nums, limit):
    s = min(nums)
    e = max(nums)
    ans = 0

    while s <= e:
        m = s + (e-s)//2

        div_sum = 0
        underLimit = True
        for i in range(len(nums)):
            if nums[i]%m == 0:
                div_sum += nums[i]//m
            else:
                div_sum += nums[i]//m + 1

            if div_sum >= limit:
                underLimit = False
                break
        
        if underLimit:
            ans = m
            e = m-1
        else:
            s = m+1

    return ans


nums = [1,2,3,4,5]
limit = 8
print(smallest_divisor_threshold_array(nums,limit))