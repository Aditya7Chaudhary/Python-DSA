def last_occurance_sorted(l,k):
    s = 0
    e = len(l)-1
    ans = e

    while s <= e:
        m = s + (e-s)//2

        if l[m] == k:
            ans = min(ans,m)
            s = m-1
            if l[s] < k:
                break
        elif l[m] < k:
            s = m+1
        else:
            e = m-1

    return ans

nums = [3, 4, 4, 5, 7, 8, 10]
x = 4
print(last_occurance_sorted(nums,x))