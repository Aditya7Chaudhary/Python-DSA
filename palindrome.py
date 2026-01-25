import math

number = int(input("Enter a number to check for palindrome: "))
num = str(number)
s = 0
e = int(math.log10(number))
f = 0

while e > s:
    if num[s] != num[e]:
        f = 1
        break
    e -= 1
    s += 1

if f==1:
    print(f"{number} is not a palindrome")
else:
    print(f"{number} is a palindrome")