import math

number = int(input("Enter a number: "))

a = number
b = 0
count = int(math.log10(a)) + 1
for i in range(count):
    b += (a%10)*(10**(count-i-1))
    a = a//10

print(b)