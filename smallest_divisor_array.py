from math import ceil

def smallest_divisor_threshold_array(nums, limit):
    s = 1
    e = max(nums)
    ans = e

    while s <= e:
        m = s + (e-s)//2

        div_sum = 0
        underLimit = True
        for i in range(len(nums)):
            div_sum += ceil(nums[i]/m)

            if div_sum > limit:
                underLimit = False
                break
        
        if underLimit:
            ans = min(ans,m)
            e = m-1
        else:
            s = m+1

    return ans


nums = [1,2,3,4,5]
limit = 8
print(smallest_divisor_threshold_array(nums,limit))