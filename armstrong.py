N = 371

a = N
x = 0
while a>0:
    x += (a%10)**3
    a //= 10
if x == N:
    print(True)
else:
    print(False)
