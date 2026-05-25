def largest_odd_number_string(s):
    ans = ""
    curr_value = ""

    for i in s:
        curr_value += i
        if int(curr_value)%2 != 0:
            ans = curr_value
        
    return ans
    
s = "4256"
print(largest_odd_number_string(s))