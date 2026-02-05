def maximum_sum(l):
    sum = l[0]
    max_sum = l[0]

    for i in range(1,len(l)):
        sum += l[i]
        if sum < 0:
            sum = 0
        
        if sum > max_sum:
            max_sum = sum

        return max_sum

l = [100,-200,100]  
print(maximum_sum(l))