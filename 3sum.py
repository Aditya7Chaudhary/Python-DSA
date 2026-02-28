def three_sum(l):
    s = 0
    m = 1
    e = len(l)-1
    l.sort()
    ans = []

    while e > m and m > s:
        sum_num = l[s]+l[m]+l[e]
        if sum_num < 0:
            if m < e-1:
                sum_num -= l[m]
                m += 1
                sum_num += l[m]
            else:
                sum_num -= l[s]
                s += 1
                sum_num += l[s]
            
        elif sum_num > 0:
            if m > s+1:
                sum_num -= l[m]
                m -= 1
                sum_num += l[m]
            else:
                sum_num -= l[e]
                e -= 1
                sum_num += l[e]

        else:
            ans.append([l[s],l[m],l[e]])
            sum_num -= l[e]
            e -= 1
            sum_num += l[e]

    return ans


l = [-1,0,1,2,-1,-4]
print(three_sum(l))
