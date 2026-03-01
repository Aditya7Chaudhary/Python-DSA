def merge_overlapping_subinterval(nums):
    l1 = nums[0]
    ans = []
    n = len(nums)

    for i in range(1,n):
        l2 = nums[i]
        if l1[1] > l2[0] and l1[1] < l2[1]:
            l1 = [l1[0],l2[1]]
            ans.append(l1)
        elif l1[1] < l2[0]:
            l1 = l2

        if l1 not in ans:
            ans.append(l1)

    return ans

nums = [[0,3],[2,6],[8,10],[15,18]]
print(merge_overlapping_subinterval(nums))