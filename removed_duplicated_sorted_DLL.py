class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
def linkedlist(l):
    head = Node(l[0])
    temp = head
    prev = None
    for i in range(1,len(l)):
        newNode = Node(l[i],prev=temp)
        temp.next = newNode
        temp = temp.next
    
    return head

def removingduplicates(head):
    temp = head.next
    while temp:
        if temp.data == temp.prev.data:
            next = temp.next
            temp.prev.next = next
            next.prev = temp.prev
            temp.next = None
            temp.prev = None
            temp = next
        else:
            temp = temp.next
    
    return head
            

def printlinkedlist(head):
    temp = head
    while temp:
        print(temp.data,end=" ")
        temp = temp.next

l = [0,0,0,1,1,1,2,2,2,4,5]
head = linkedlist(l)
printlinkedlist(head)
print()
head = removingduplicates(head)
printlinkedlist(head)