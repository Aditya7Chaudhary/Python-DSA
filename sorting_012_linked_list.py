class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
        
def linkedlist(l):
    head = Node(l[0])
    temp = head
    for i in range(1,len(l)):
        temp.next = Node(l[i])
        temp = temp.next
    
    return head

def sorting(head):
    temp = head
    temp1 = None
    temp2 = None
    while temp:
        if temp.data == 0:
            if temp2:
                temp2.next = temp.next
                temp.next = head
                head = temp
                temp = temp2.next
            elif temp1:
                temp1.next = temp.next
                temp.next = head
                head = temp
                temp = temp1.next
            else:
                temp = temp.next
        elif temp.data == 1:
            if temp1 and temp2:
                temp2.next = temp.next
                temp.next = temp1.next
                temp1.next = temp
                temp = temp2.next
                temp1 = temp1.next
            elif temp2:
                temp2.next = temp.next
                if head.data == 2:
                    temp.next = head
                    head = temp
                else:
                    curr = head
                    while curr.next.data == 0:
                        curr = curr.next
                    temp.next = curr.next
                    curr.next = temp
                temp1 = temp
                temp = temp2.next
            else:
                temp1 = temp
                temp = temp.next
        else:
            temp2 = temp
            temp = temp.next
            
    return head

def printlinkedlist(head):
    temp = head
    while temp:
        print(temp.data,end=" ")
        temp = temp.next

l = [2,1,0,0,2,1,2]
head = linkedlist(l)
printlinkedlist(head)
print()
head = sorting(head)
printlinkedlist(head)