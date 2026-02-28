def majority_elements(l):
    num1 = None
    num2 = None
    count1 = 0
    count2 = 0
    n = len(l)

    for i in l:
        if num1 == None and i != num2:
            num1 = i
            count1 += 1
        elif num2 == None and i != num1:
            num2 = i
            count2 += 1
        else:
            if i == num1:
                count1 += 1
            elif i == num2:
                count2 += 1
            elif count1 == 0:
                num1 = i
                count1 = 1
            elif count2 == 0:
                num2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        print(num1,num2)

    count1,count2 = 0,0
    for i in l:
        if i == num1:
            count1 += 1
        elif i == num2:
            count2 += 1
    
    if count1 > n//3 and count2 > n//3:
        return [num1,num2]
    elif count1 > n//3:
        return [num1]
    elif count2 > n//3:
        return [num2]
    else:
        return []

l = [1,1,1,2,3,7,8,1,6,9]
print(majority_elements(l))