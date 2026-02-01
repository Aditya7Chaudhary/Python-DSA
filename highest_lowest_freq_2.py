# Brute force

def highest_lowest_freq(l,k):
    l.sort()
    ans = 1

    for i in range(len(l)):
        a = 0
        j = 0
        while (i - j) >= 0:
            cost = l[i] - l[i-j]
            if a + cost > k:
                break
            a += cost
            j += 1
            
        ans = max(ans, j)
        
    return ans
                    

l = [1,2,4]
k = 5
print(highest_lowest_freq(l,k))


# Optimal (Sliding Window)

def highest_lowest_freq_optimized(nums, k):
    nums.sort()
    left = 0
    total = 0
    ans = 0
    
    # 'right' expands the window
    for right in range(len(nums)):
        # Add the new number to our window sum
        total += nums[right]
        
        # LOGIC:
        # We want to make all numbers in the window [left...right] equal to nums[right].
        # The cost is: (target * count) - (current_sum)
        # Cost = (nums[right] * window_length) - total
        
        while (nums[right] * (right - left + 1)) - total > k:
            # If cost is too high, shrink window from the left
            total -= nums[left]
            left += 1
            
        # Update max window size found so far
        ans = max(ans, right - left + 1)
        
    return ans

print(highest_lowest_freq_optimized(l, k))