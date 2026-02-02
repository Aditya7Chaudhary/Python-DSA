def check_sorted(l):
    for i in range(1,len(l)):
        if l[i] < l[i-1]:
            return False
        
    return True

l = [1,2,3,3,5,2]
print(check_sorted(l))