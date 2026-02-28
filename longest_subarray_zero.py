def longest_subarray_zero(l):
    max_array = []
    current_array = []
    sums = {}
    n = len(l)

    for i in range(n):
        current_array = l[:i+1] 
        current_sum = sum(current_array)

        if current_sum > 0 and current_sum in sums:
            current_array = l[sums[current_sum]:i+1]
            current_sum = sum(current_array)

        if current_sum == 0:
            if len(max_array) < len(current_array):
                max_array = current_array
            break
            
        sums[current_sum] = i

    return max_array

l = [6, -2, 2, -8, 1, 7, 4, -10]
print(longest_subarray_zero(l))