# Assuming the array does not have duplicates

def number_times_sorted_array_rotated(l):
    s = 0
    e = len(l)-1

    if l[s] <= l[e]:
        return 0

    while s <= e:
        m = s + (e-s)//2

        if l[m] < l[m-1] and m != 0:
            return m
        if l[m] > l[e]:
            s = m+1
        else:
            e = m-1

nums = [5,3]
print(number_times_sorted_array_rotated(nums))      