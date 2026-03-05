def capacity_packages_set_days(weights, days):
    s = max(weights)
    e = sum(weights)
    n = len(weights)
    ans = e

    while s <= e:
        m = s + (e-s)//2

        curr_weight = 0
        day = 0
        for i in range(n):
            curr_weight += weights[i]

            if curr_weight == m:
                curr_weight = 0
                day += 1
            elif curr_weight > m:
                curr_weight = weights[i]
                day += 1
        
        if curr_weight > 0:
            day += 1

        if day <= days:
            e = m-1
            ans = min(ans,m)  
        else:
            s = m+1

    return ans

weights = [5, 4, 5, 2, 3, 4, 5, 6]
days = 5
print(capacity_packages_set_days(weights, days))      