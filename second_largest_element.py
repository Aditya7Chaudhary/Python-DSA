def second_largest_element(l):
    max = float('-inf')
    sec_max = float('-inf')

    for i in l:
        if i > max:
            sec_max = max
            max = i
        elif sec_max < i and max != i:
            sec_max = i
    
    return sec_max

l = [10,5,3,7,6,1,2]
print(second_largest_element(l))