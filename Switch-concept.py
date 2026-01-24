print("A concept similar to if-else but for simplar cases \n")

num = int(input("Enter a number from 1 to 7: "))

match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

"""

Limited to Integer or Character Types
Switch statements are exclusively designed to handle integer or character values. 
Ensure that the expression provides values of type int or char

"""