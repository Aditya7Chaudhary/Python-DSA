N = 36

import math

l = []
for i in range(1,int(N**0.5)+1):
    if N%i == 0:
        if N//i == i:
            l.append(i)
        else:
            l.extend([i,N//i])
l.sort()
print(l)