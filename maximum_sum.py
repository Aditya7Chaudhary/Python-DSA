def maximum_sum(l):
    sum = 0

    for i in range(len(l)):
        sum += l[i]
        if sum < 0:
            sum = 0

        return sum

l = [100,-200,100]  
print(maximum_sum(l))