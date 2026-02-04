def two_sum(l,target):
    seen = {}
    for index, val in enumerate(l):
        diff = target - val

        if diff in seen:
            return [seen[diff],index]
        
        seen[val] = index

    return [-1,-1]

l = [3,2,4]
N = 6
print(two_sum(l,N))