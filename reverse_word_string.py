def reverse_word_string(s):
    i,e = len(s)-1,len(s)
    j = e+1
    ans = ""
    s += " "

    while i > 0:
        if s[i] == " ":
            ans += s[j:e+1]
            e = i
        else:
            j = i
        i -= 1

    ans += s[i:e]
    return ans

s = "      Welcome                           to             the      jungle      "
print(reverse_word_string(s))