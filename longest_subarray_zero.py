def longest_subarray_zero(l):
    max_array = 0
    left = 0
    right = 0
    current_sum = 0
    sums = {}
    n = len(l)

    for i in range(n): 
        current_sum += l[i]

        if current_sum == 0:
            max_array = i+1
            right = i+1
            left = 0
        elif current_sum != 0 and current_sum in sums:
            if max_array < i+1 - sums[current_sum]:
                left = sums[current_sum]+1
                right = i+1
                max_array = right - left
        else:
            sums[current_sum] = i

    return l[left:right]

l = [6, -2, 2]
print(longest_subarray_zero(l))