def largest_element(l):
    max = 0
    for i in l:
        if i > max:
            max = i
    return max 

l = [3,2,5,4,2,6]
print(largest_element(l))

# Time complexity is O(n)