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

# To only show the Kth row

def kth_pascals_triangle(K):
    def get_nCr(n,r):
        res = 1
        # Math optimization: nCr is perfectly equal to nC(n-r). 
        # If n=10 and r=8, 10C8 is the same as 10C2. We pick the smaller one to loop less!
        if r > n - r:
            r = n - r
            
        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1) # Use integer division
            
        return res
    
    l = []
    
    for i in range(k+1):
        l.append(get_nCr(k,i))

    return l

k = 5
print(kth_pascals_triangle(k))