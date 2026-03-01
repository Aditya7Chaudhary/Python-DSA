def repeating_missing_numbers(l):
    n = len(l)
    sum_n = n*(n+1)//2
    sum_l = sum(l)
    sq_n = n*(n+1)*(2*n+1)//6
    sq_l = 0
    for i in l:
        sq_l += i*i
    
    diff_ab = sum_n - sum_l
    add_ab = (sq_n - sq_l)//diff_ab

    B = (diff_ab + add_ab)//2
    A = add_ab - B

    return [A,B]

nums = [1, 2, 3, 6, 7, 5, 7]
print(repeating_missing_numbers(nums))