def painters_partition_problem(l,k):
    s = max(l)
    e = sum(l)

    while s <= e:
        m = s + (e-s)//2

        array_sum, c_k = 0,0
        for i in l:
            array_sum += i
            if array_sum == m:
                c_k += 1
                array_sum = 0
            elif array_sum > m:
                c_k += 1
                array_sum = i
        
        if array_sum > 0:
            c_k += 1
        
        if c_k <= k:
            e = m-1
        else:
            s = m+1

    return s

l = [10, 20, 30, 40]
k = 2
print(painters_partition_problem(l,k))