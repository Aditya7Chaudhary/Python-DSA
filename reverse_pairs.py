def reverse_pairs(l):
    def merge(l,s,m,e,ans):
        left = s
        right = m+1
        temp = []

        while left <= m and right <= e:
            if l[left] <= l[right]:
                temp.append(l[left])
                left += 1
            else:
                temp.append(l[right])
                right += 1
                if l[right]*2 < l[left]:
                    ans += (m - left + 1)

        if left <= m:
            temp.extend(l[left:m+1])
        elif right <= e:
            temp.extend(l[right:e])

        l[s:e+1] = temp
        
        return l,ans
    
    def divide(l,s,e,ans):
        if s >= e:
            return l,ans
        m = s + (e-s)//2
        l,ans = divide(l,s,m,ans)
        l,ans = divide(l,m+1,e,ans)
        l,ans = merge(l,s,m,e,ans)
        
        return l, ans

    ans = 0
    s = 0
    e = len(l)-1
    return divide(l,s,e,ans)

l = [1,3,2,3,1]
print(reverse_pairs(l))