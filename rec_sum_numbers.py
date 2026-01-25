def sum_numbers(sum,x):
    
    if x == 0:
        return 0

    sum = x + sum_numbers(sum,x-1)
        
    return sum

print(sum_numbers(0,5))