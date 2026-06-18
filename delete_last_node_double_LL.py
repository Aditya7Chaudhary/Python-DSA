class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
def doublelinkedlist(l):
    head = Node(l[0])
    temp = head
    
    for i in range(1,len(l)):
        newNode = Node(l[i],prev=temp)
        temp.next = newNode

        temp = temp.next
    
    return head

def dellastnode(head):
    temp = head
    
    while temp:
        if not temp.next:
            temp.prev.next = None
        temp = temp.next

def printlinkedlist(head):
    temp = head
    
    while temp:
        if temp.next:
            print(temp.data,end=" <-> ")
        else:
            print(temp.data)
        temp = temp.next
    

l = [3,2,8,9,1]
head = doublelinkedlist(l)
printlinkedlist(head)
dellastnode(head)
printlinkedlist(head)