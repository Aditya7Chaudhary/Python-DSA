def majority_element(l):
    count = 0
    ans = l[0]
    for i in range(1,len(l)):
        if l[i] == ans:
            count += 1
        else:
            if count > 0:
                count -= 1
            else:
                ans = l[i]

    return ans

l = [7, 0, 0, 1, 7, 7, 2, 7, 7] 
print(majority_element(l))