def min_max_dist_gas_station(l, k):
    n = len(l)
    low = 0
    high = 0
    for i in range(n - 1):
        high = max(high, l[i+1] - l[i])

    for _ in range(100):
        mid = (low + high) / 2.0
        count = 0
        for i in range(n - 1):
            dist = l[i+1] - l[i]
            count += int(dist / mid)
            if dist / mid == int(dist / mid):
                count -= 1
        
        if count > k:
            low = mid
        else:
            high = mid
            
    return high

l = [1, 2, 3, 4, 5]
k = 4
print(min_max_dist_gas_station(l, k))