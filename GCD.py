import math

# Base approach

N1 = 108
N2 = 12

for i in range(1,(min(N1,N2))+1):
    if N1%i == 0 and N2%i == 0:
        ans = i
print(ans)

# Optimal approach

x = N1
y = N2

while x > 0:
    c = x
    x = max(x,y) - min(x,y)
    y = c
print(y)