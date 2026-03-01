def merge_overlapping_subinterval(nums):
    nums.sort()
    ans = [nums[0]]
    n = len(nums)

    for i in range(1,n):
        curr_array = nums[i]
        last_array = ans[-1]

        if last_array[1] >= curr_array[0]:
            last_array[1] = max(last_array[1],curr_array[1])
        else:
            ans.append(curr_array)

    return ans

nums = [[1, 3], [2, 4], [3, 5]]
print(merge_overlapping_subinterval(nums))