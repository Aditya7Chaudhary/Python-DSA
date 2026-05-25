def reverse_word_string(s):
    i,e = len(s)-1,len(s)
    ans = ""

    while i > 0:
        if s[i] == " ":
            ans += s[i+1:e] + " "
            e = i
        i -= 1

    ans += s[i:e]
    return ans

s = "Welcome to the jungle"
print(reverse_word_string(s))