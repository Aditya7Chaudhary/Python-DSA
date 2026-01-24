# Pattern 1

for i in range(5):
    print("*"*5)

# Pattern 2

for i in range(5):
    print("*"*(i+1))

# Pattern 3

for i in range(5):
    for j in range(i+1):
        print(j+1, end="")
    print("\n")

# Pattern 4

for i in range(5):
    for j in range(i+1):
        print(i+1, end="")
    print("\n")

# Pattern 5

for i in range(5):
    print("*"*(5-i))

# Pattern 6

for i in range(5):
    for j in range(5-i):
        print(j+1,end="")
    print("\n")

# Pattern 7

for i in range(5):
    print(" "*(5-i-1)+"*"*(2*i+1))
print('\n')

# Pattern 8

for i in range(5):
    print(" "*i+"*"*(2*(4-i)+1))
print('\n')

# Pattern 9

for i in range(5):
    print(" "*(5-i-1)+"*"*(2*i+1))
for i in range(4):
    print(" "*(i+1)+"*"*(2*(3-i)+1))
print('\n')

# Pattern 10

for i in range(5):
    print("*"*(i+1))
for i in range(4):
    print("*"*(4-i))
print('\n')

# Pattern 11

for i in range(5):
    for j in range(i+1):
        if (i-j)%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print('\n')
print('\n')

# Pattern 12

for i in range(4):
    for j in range(i+1):
        print(j+1,end="")
    print(" "*2*(3-i),end="")
    for j in range(i+1):
        print(i-j+1,end="")
    print('\n')
    
# Pattern 13

a = 1
for i in range(5):
    for j in range(i+1):
        print(a,end=" ")
        a += 1
    print('\n')

# Pattern 14

l = ['A','B','C','D','E']
for i in range(5):
    for j in range(i+1):
        print(l[j],end="")
    print('\n')
print('\n')

# Pattern 15

l = ['A','B','C','D','E']
for i in range(5):
    for j in range(5-i):
        print(l[j],end="")
    print('\n')
print('\n')

# Pattern 16

for i in range(5):
    for j in range(i+1):
        print(l[i],end="")
    print('\n')
print('\n')

# Pattern 17

for i in range(4):
    print(" "*(3-i), end="")
    for j in range(i+1):
        print(l[j], end="")
    for j in range(1,i+1):
        print(l[i-j], end="")
    print('\n')
print('\n')

# Pattern 18

for i in range(5):
    for j in range(i+1):
        print(l[4+j-i],end="")
    print('\n')
print('\n')

# Pattern 21

for i in range(4):
    if i in [0,3]:
        print("*"*4)
    else:
        print("*"+" "*2+"*")
print("\n")

# Pattern 22

for i in range(7):
    for j in range(7):
        dist_i = abs(i - 3)
        dist_j = abs(j - 3)
        
        value = max(dist_i, dist_j) + 1
        
        print(value, end=" ")
    print()