# XOR strategy
# a^a = 0
# a^0 = a

def single_number(l):
    xor = 0
    for i in l:
        xor ^= i
    
    return xor

l = [2,2,0,1,0]
print(single_number(l))