def rec_palindrome_str(s):
    if len(s) <= 1:
        return True
    
    if not s[0].isalpha():
        return rec_palindrome_str(s[1:])
    
    if not s[-1].isalpha():
        return rec_palindrome_str(s[:-1])

    if s[0].lower() != s[-1].lower():
        return False
    else:
        return rec_palindrome_str(s[1:-1])
    
s = "a nna"
print(rec_palindrome_str(s))