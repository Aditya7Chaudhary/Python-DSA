def kth_element_two_sorted_arrays(nums1,nums2,k):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m = len(nums1)
    n = len(nums2)

    s = 0
    e = m

    while s <= e:
        p1 = s + (e-s)//2
        p2 = k - p1

        maxleft1 = float("-inf") if p1 == 0 else nums1[p1-1]
        minright1 = float("-inf") if p1 == m else nums1[p1]
        maxleft2 = float("-inf") if p2 == 0 else nums2[p2-1]
        minright2 = float("-inf") if p2 == m else nums2[p2]

        if maxleft1 <= minright2 and maxleft2 <= minright1:
            return max(maxleft1,maxleft2)
        else:
            e = p1 - 1
            s = p1 + 1
    

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5  
print(kth_element_two_sorted_arrays(a,b,k))

