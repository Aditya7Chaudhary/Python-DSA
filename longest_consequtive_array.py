def longest_consequtive_array(l):
    l.sort()
    count = 1
    for i in range(1,len(l)):
        if l[i-1]+1 == l[i]:
            count += 1
        else:
            count = 1

    return count

l = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longest_consequtive_array(l))