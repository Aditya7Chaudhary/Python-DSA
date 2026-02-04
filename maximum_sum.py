def maximum_sum(l):
    left = 0
    right = len(l)-1

    sum = 0
    for i in range(len(l)):
        sum += l[i]
    max_sum = sum

    while left < right:
        if l[left] < l[right]:
            sum -= l[left]
            left += 1
        else:
            sum -= l[right]
            right -= 1
        
        if max_sum < sum:
            max_sum = sum

    return max_sum

l = [2, 3, 5, -2, 7, -4]  
print(maximum_sum(l))