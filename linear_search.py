def linear_search(l,N):
    if N in l:
        return l.index(N)
    else:
        return False
    
N = 5
l = [2,6,2,4,3,6,7,2]

print(linear_search(l,N))