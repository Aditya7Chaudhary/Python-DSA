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