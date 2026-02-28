def pascals_triangle(k):

    l = [1]
    for i in range(1,k):
        print(l)
        l_copy = [1]
        for j in range(i):
            l_copy.append(sum(l[j:j+2]))
        l = l_copy

    print(l)
    return l

k = 6
print("kth row is :",pascals_triangle(k))