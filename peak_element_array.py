# The array is actually sorted in intervals except for the peak elements in some index

def peak_element_array(l):
    s = 0
    e = len(l)-1

    while s <= e:
        m = s + (e-s)//2

        if l[m+1] < l[m] and l[m] > l[m-1]:
            return m
        elif l[s] >= l[m-1]:
            e = m-1
        elif l[m+1] >= l[e]:
            s = m+1
        else:
            s += 1
            e -= 1

    return len(l)-1

nums = [1,2,1,3,5,6,4]
print(peak_element_array(nums))