def missing_number(l,N):
    sum1 = N*(N+1)//2
    sum2 = sum(l)
    
    return sum1 - sum2

l = [3,0,1]
N = 3

print(missing_number(l,N))