def last_occurance_sorted(l,k):
    def bounds(isFirst):
        s = 0
        e = len(l)-1
        bound = -1

        while s <= e:
            m = s + (e-s)//2

            if l[m] == k:
                bound = m
                if isFirst:
                    e = m-1
                else:
                    s = m+1
            elif l[m] < k:
                s = m+1
            else:
                e = m-1

        return bound

    lower_bound = bounds(True)
    upper_bound = bounds(False)

    if lower_bound == -1 or upper_bound == -1:
        return [-1,-1]
    else:
        return [lower_bound,upper_bound]

nums = [5,7,7,8,8,10]
x = 8
print(last_occurance_sorted(nums,x))