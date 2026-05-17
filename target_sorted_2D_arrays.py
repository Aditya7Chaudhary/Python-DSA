def target_sorted_2D_arrays(nums,target):
    if len(nums) == 0:
        return False
    
    s = 0
    e = len(nums)-1
    
    while s < e:
        m = s + (e-s+1)//2
        if nums[m][0] < target:
            s = m
        elif nums[m][0] > target:
            e = m-1
        else:
            return True
        
    i = s
    s = 0
    e = len(nums[0])-1

    while s <= e:
        m = s + (e-s)//2
        if nums[i][m] < target:
            s = m+1
        elif nums[i][m] > target:
            e = m-1
        else:
            return True
    
    return False

nums = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
target = 8

print(target_sorted_2D_arrays(nums,target))