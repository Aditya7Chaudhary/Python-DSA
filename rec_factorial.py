def rec_factorial(N):
    if N == 1:
        return 1
    
    return N*rec_factorial(N-1)

print(rec_factorial(5))