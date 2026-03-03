def single_element_sorted_array(l):
    s = 0
    e = len(l)-1

    while s <= e:
        m = s + (e-s)//2
        
        if m != 0 and l[m-1] == l[m]:
            if m%2 == 0:
                e = m-1
            else:
                s = m+1   
        elif m != len(l)-1 and l[m] == l[m+1]:
            if m%2 == 0:
                s = m+1
            else:
                e = m-1
        else:
            return l[m]
        
nums = [1,1,2,2,3]
print(single_element_sorted_array(nums))