def rearrange_list(l):
    ans = [0]*len(l)
    a = 0
    b = 1
    for i in range(len(l)):
        if l[i] > 0:
            ans[a] += l[i]
            a += 2
        else:
            ans[b] += l[i]
            b += 2
    return ans

l = [1,2,-3,-1,-2,3]
print(rearrange_list(l))