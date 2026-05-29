def roman_number_value(s):
    ans = 0
    n = len(s)
    s += "_"

    for i in range(n):
        if s[i] == 'M':
            ans += 1000
        elif s[i] == 'C':
            if s[i+1] == 'M':
                ans -= 100
            else:
                ans += 100
        elif s[i] == 'L':
            ans += 50
        elif s[i] == 'X':
            if s[i+1] == 'C' or s[i+1] == 'L':
                ans -= 10
            else:
                ans += 10
        elif s[i] == 'V':
            ans += 5
        elif s[i] == 'I':
            if s[i+1] == 'V' or s[i+1] == 'X':
                ans -= 1
            else:
                ans += 1
    
    return ans

s = "MCMXCIV"
print(roman_number_value(s))