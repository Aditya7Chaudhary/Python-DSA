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

def reversedoubleLL(head):
    temp = head
    while temp:
        if not temp.next:
            newhead = temp
        temp.next, temp.prev = temp.prev, temp.next
        temp = temp.prev
            
    return newhead

def printlinkedlist(head):
    temp = head
    while temp:
        if temp.next:
            print(temp.data,end=" <-> ")
        else:
            print(temp.data)
        temp = temp.next
        
l = [2,6,3,8,3]
head = doublelinkedlist(l)
printlinkedlist(head)
head = reversedoubleLL(head)
printlinkedlist(head)