def majority_elements(l):
    num1 = None
    num2 = None
    count1 = 0
    count2 = 0
    n = len(l)

    for i in l:
        if num1 == None:
            num1 = i
            count1 += 1
        elif num2 == None:
            num2 = i
            count2 += 1
        else:
            if i in (num1,num2):
                if i == num1:
                    count1 += 1
                else:
                    count2 += 1
            else:
                if count1 >= count2:
                    count1 -= 1
                else:
                    count2 -= 1

        if count1 == 0:
            num1 = i
            count1 += 1
        elif count2 == 0:
            num2 = i
            count2 += 1

    if count1 > 1 and count2 > 1:
        return num1,num2
    elif count1 > 1:
        return num1
    else:
        return num2
    
l = [1,2,1,1,3,2,2]
print('\n',majority_elements(l))