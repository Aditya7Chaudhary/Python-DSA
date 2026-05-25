def remove_outermost_paranthese(s):
    ans = ""
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] == "(":
            count += 1
        elif s[i] == ")":
            count -= 1

        if count > 1:
            ans += s[i]
        elif count == 1 and s[i] == ")":
            ans += s[i]
    
    return ans

s = "(()())(())(()(()))"
print(remove_outermost_paranthese(s))
