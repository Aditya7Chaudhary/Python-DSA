def merge(l,s,m,e):
    l_ans = []
    s1 = 0
    s2 = 0
    for i in range(e):
        if len(l[s]) == s1:
            l_ans.extend(l2)
            break
        if len(l2) == s2:
            l_ans.extend(l1)
            break

        if l1[s1] >= l2[s2]:
            l_ans.append(l2[s2])
            s2 += 1            
        else:
            l_ans.append(l1[s1])
            s1 += 1
    
    return l_ans

def merge_sort(l,s,e):
    if s > e:
        return 
    m = s + (e-s)//2
    merge_sort(l,s,m)
    merge_sort(l,m+1,e)
    merge(l,s,m,e)
    
l = [3,1,2,4,1,5,2,6,4]
print(merge_sort(l,0,len(l)-1))
