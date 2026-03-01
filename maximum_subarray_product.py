def maximum_subarray_product(l):
    l_0,l_neg = [],[]
    n = len(l)
    neg_num = 0
    for i in range(n):
        if l[i] < 0:
            neg_num += 1
        elif l[i] == 0:
            l_0.append(i)
            l_neg.append(neg_num)
            neg_num = 0
    l_neg.append(neg_num)
    l_0.append(n)

    max_product = 0
    for i in range(len(l_neg)):
        product = 1
        for j in range(l_0[i]):
                product *= l[j]
        if l_neg[i]%2 == 0:
            max_product = max(max_product,product)
        else:
            if i > 0:
                s = l_0[i-1]
            else:
                s = 0
            e = l_0[i]

            while s < e:
                if l[s] < 0 and l[e] < 0:
                    if l[e] < l[s]:
                        product /= l[s]
                        break
                    else:
                        product /= l[e]
                        break
                elif l[s] < 0:
                    product /= l[s]
                    break
                elif l[e] < 0:
                    product /= l[e]
                    break
                else:
                    if l[s] < l[e]:
                        product /= l[s]
                        s += 1
                    else:
                        product /= l[e]
                        e -= 1

            max_product = max(max_product,product)
    
    return max_product

nums = [-1]
print(maximum_subarray_product(nums))