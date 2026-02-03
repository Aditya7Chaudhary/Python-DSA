def remove_duplicates(l):
    lu = [l[0]]
    for i in range(1,len(l)):
        if l[i] != l[i-1]:
            lu.append(l[i])
    return lu

l = [1,2,2,3,3,5,6,7,7]
print(remove_duplicates(l))