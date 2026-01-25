# Cheeky way

number = str(input("Enter a number: "))
print(len(number))

# Actual way

num = int(input("Enter a number: "))
a = num
count = 0
while a > 0:
    count += 1
    a = a//10
print(count)