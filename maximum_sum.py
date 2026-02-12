def maximum_sum(l):
    sum = l[0]
    max_sum = l[0]
    l_ans = []

    for i in range(1,len(l)):
        sum += l[i]
        l_ans.append(l[i])
        if sum < 0:
            sum = 0
            l_ans = []
        
        if sum > max_sum:
            max_sum = sum
            

    return max_sum, l_ans

l = [2, 3, 5, -2, 7, -4]  
print(maximum_sum(l))