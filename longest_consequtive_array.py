# Good Approach

def longest_consequtive_array(l):
    l.sort()
    count = 1
    for i in range(1,len(l)):
        if l[i-1]+1 == l[i]:
            count += 1
        else:
            count = 1

    return count

# Best Approach

def longest_consequtive_array_opt(l):
    st = set()
    for i in l:
        st.add(i)
    
    ans = 1
    min_num_l = []
    
    for i in range(len(st)):
        if l[i]-1 not in st:
            min_num_l.append(i)
    
    for i in min_num_l:
        count = 1
        num = l[i]+1
        while num in st:
            count += 1
            num += 1
        if count > ans:
            ans = count
                   
    return ans



l = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longest_consequtive_array(l))
print(longest_consequtive_array_opt(l))