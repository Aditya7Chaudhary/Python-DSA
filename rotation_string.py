def rotation_string(s,goal):
    n = len(s)
    
    for i in range(n):
        if s[i:] + s[:i] == goal:
            return True
    
    return False

s = "abcde"
goal = "cdeab"
print(rotation_string(s,goal))