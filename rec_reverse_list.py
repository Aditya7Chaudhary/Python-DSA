def rec_reverse_list(l):
    if len(l) < 1:
        return []

    return rec_reverse_list(l[1:]) + [l[0]]

l = [1,2,3,4,5,6]
print(rec_reverse_list(l))