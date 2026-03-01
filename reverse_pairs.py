def reverse_pairs(l):
    def merge(l,s,m,e,ans):
        left = s
        right = m+1
        temp = []

        while left <= m and right <= e:
            if l[right]*2 < l[left]:
                ans += (m+1 - left)
                right += 1
            else:
                left += 2
        
        left = s
        right = m+1

        while left <= m and right <= e:
            if l[left] < l[right]:
                temp.append(l[left])
                left += 1
            elif l[left] == l[right]:
                temp.extend([l[left],l[right]])
                left += 1
                right += 1
            else:
                temp.append(l[right])
                right += 1

        if left <= m:
            temp.extend(l[left:m+1])
        elif right <= e:
            temp.extend(l[right:e+1])

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
    l,ans = divide(l,s,e,ans)

    return ans

l = [1,3,2,3,1]
print(reverse_pairs(l))