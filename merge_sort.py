class Solution:
    def merge(self,l,s,m,e):
        temp = []
        left = s
        right  = m+1

        while left <= m and right <= e:
            if l[left] <= l[right]:
                temp.append(l[left])
                left += 1
            else:
                temp.append(l[right])
                right += 1

        while left <= m:
            temp.append(l[left])
            left += 1
        while right <= e:
            temp.append(l[right])
            right += 1

        for i in range(s,e+1):
            l[i] = temp[i-s]
        

    def merge_sort(self,l,s,e):
        if s >= e:
            return 
        m = s + (e-s)//2
        self.merge_sort(l,s,m)
        self.merge_sort(l,m+1,e)
        self.merge(l,s,m,e)
    
l = [3,2,4,1,5,2,6,4]
sol = Solution()
sol.merge_sort(l, 0, len(l) - 1)
print(l)
