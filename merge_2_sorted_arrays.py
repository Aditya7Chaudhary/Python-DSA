def merge_two_sorted_arrays(n1,n2):
    n = len(n2)
    m = len(n1)-n-1

    i = len(n1)-1
    j = n-1
    while i >= 0 and j >= 0:
        if m >= 0 and n1[m] > n2[j]:
            n1[i] = n1[m]
            m -= 1
        else:
            n1[i] = n2[j]
            j -= 1
        i -= 1

    return n1

nums1 = [-5, -2, 4, 5, 0, 0, 0]
nums2 = [-3, 1, 8]
print(merge_two_sorted_arrays(nums1,nums2))