
def rec_name(x,name):
    print(name, end=" ")
    x += 1
    if x <= 3:
        rec_name(x,name)
    else:
        return

x = 1
name = "Aditya"
rec_name(x,name)