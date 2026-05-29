def maximum_depth_strings(s):
    value = 0
    max_ans = 0
    for i in s:
        if i == "(":
            value += 1
        elif i == ")":
            max_ans = max(max_ans,value)
            value -= 1

    return max_ans

s = "(1+(2*3)+((8)/4))+1"
print(maximum_depth_strings(s))