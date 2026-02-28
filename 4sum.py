def four_sum(l, target):
    n = len(l)
    l.sort()
    ans = []

    for i in range(n):
        if i > 0 and l[i] == l[i-1]:
            continue

        for j in range(i+1,n):
            if j > i+1 and l[j] == l[j-1]:
                continue

            left = j+1
            right = n-1

            while left < right:
                total_sum = l[i] + l[j] + l[left] + l[right]
                
                if total_sum > target:
                    right -= 1
                elif total_sum < target:
                    left += 1
                else:
                    ans.append([l[i],l[j],l[left],l[right]])
                    left += 1
                    right -= 1

                    while left < right and l[left] == l[left-1]:
                        left += 1
                    while left < right and l[right] == l[right+1]:
                        right -= 1

    return ans

l = [4,3,3,4,4,2,1,2,1,1]
target = 9
# Output = [[1,1,3,4],[1,2,2,4],[1,2,3,3]]
print(four_sum(l,target))