def rec_number(count, N):
    if N > count:
        return

    print(count)

    rec_number(count-1,N)

N = 1
count = 4
rec_number(count,N)