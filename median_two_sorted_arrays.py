from math import floor, ceil

def median_two_sorted_arrays(nums1,nums2):
    m = len(nums1)
    n = len(nums2)
    if m > n:
        nums1, nums2 = nums2, nums1
    
    s = 0
    e = m

    while s <= e:
        partition_1 = s + (e-s)//2
        partition_2 = (m + n + 1)//2  - partition_1

        maxLeftX = float('-inf') if partition_1 == 0 else nums1[partition_1 - 1]
        minRightX = float('inf') if partition_1 == m else nums1[partition_1]

        maxLeftY = float('-inf') if partition_2 == 0 else nums2[partition_2 - 1]
        minRightY = float('inf') if partition_2 == n else nums2[partition_2]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (m + n) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            else:
                return float(max(maxLeftX, maxLeftY))
        elif maxLeftX > minRightY:
            e = partition_1 - 1
        else:
            s = partition_1 + 1


nums1 = [1,2]
nums2 = [3,4]
print(median_two_sorted_arrays(nums1,nums2))