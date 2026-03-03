# The array is actually sorted in intervals except for the peak elements in some index

def peak_element_array(l):
    s = 0
    e = len(l)-1

    while s <= e:
        m = s + (e-s)//2

        if l[m] > l[m+1]:
            e = m-1
        else:
            s = m+1
    
    return s

nums = [3,4,3,2,1]
print(peak_element_array(nums))