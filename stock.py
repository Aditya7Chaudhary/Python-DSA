def stock(l):
    i = 0
    profit = 0
    for j in range(len(l)):
        if l[i] > l[j]:
            i = j
        else:
            profit = max(profit,l[j] - l[i])

    return profit

l = [7,1,5,3,6,4]
print(stock(l))