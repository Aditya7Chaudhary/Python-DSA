def three_sum(l):
    n = len(l)
    l.sort()
    ans = []
    
    for i in range(n):
        if i > 0 and l[i] == l[i-1]:
            continue

        k = -l[i]
        left = i+1
        right = n-1

        while left < right:
            sum_num = l[left] + l[right]
            if sum_num > k:
                right -= 1
            elif sum_num < k:
                left += 1
            else:
                ans.append([-k,l[left],l[right]])
                left += 1
                right -= 1

                while left < right and l[left] == l[left-1]:
                    left += 1
                while left < right and l[right] == l[right+1]:
                    right -= 1
        
    return ans


l = [-1,0,1,2,-1,-4]
print(three_sum(l))
