# Basic
def fibonacci(x):
    l = [0,1]
    if x == 0:
        return 0
    if x == 1:
        return 1
    
    for i in range(2,x+1):
        l.append(l[i-1]+l[i-2])
    return l[i]

# Optimal
def rec_fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    
    return rec_fibonacci(x-1) + rec_fibonacci(x-2)


print(fibonacci(6))
print(rec_fibonacci(6))