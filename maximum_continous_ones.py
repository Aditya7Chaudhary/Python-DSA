def max_cont_ones(l):
    ans = 0
    final_ans = 0
    for i in range(len(l)):
        if l[i] == 1:
            ans += 1
        else:
            ans = 0

        if ans > final_ans:
            final_ans = ans

    return final_ans


l = [1,1,1,1,1,0,0,1,1,1,1]
print(max_cont_ones(l))