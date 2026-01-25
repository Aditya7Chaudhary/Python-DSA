# Brute force

num = int(input("Enter a number: "))
a = num
count = 0
while a > 0:
    count += 1
    a = a//10
print(count)

# Optimal

from math import log10

print(int(log10(num))+1)