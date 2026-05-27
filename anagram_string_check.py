def anagram_string_check(s,goal):
    m1 = [0]*256
    m2 = [0]*256

    n = len(s)
    for i in range(n):
        m1[ord(s[i])] += 1
        m2[ord(goal[i])] += 1
    
    if m1 == m2:
        return True
    else:
        return False
    
s = "anagram"
t = "nagaram"
print(anagram_string_check(s,t))