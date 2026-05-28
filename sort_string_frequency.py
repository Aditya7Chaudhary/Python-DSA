def sort_string_frequency(s):
    n = len(s)
    m = []

    for i in range(ord('z')-ord('A')+1):
        m.append([0,chr(i+ord('A'))])

    for i in range(n):
        m[ord(s[i])-ord('A')][0] += 1

    m.sort(key = lambda x: x[0], reverse = True)

    ans = ""
    for i in range(n):
        ans += m[i][1]*m[i][0]

    return ans

s = "tree"
print(sort_string_frequency(s))