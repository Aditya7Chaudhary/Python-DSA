def rec_number(count, N):
    if N < count:
        return

    print(count)

    rec_number(count+1,N)

N = 4
count = 1
rec_number(count,N)