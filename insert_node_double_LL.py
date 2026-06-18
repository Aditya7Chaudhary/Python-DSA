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

def addingNode(head,num):
    temp = head
    while temp:
        if not temp.next:
            newNode = Node(num,prev=temp)
            temp.next = newNode
            break
        temp = temp.next
        
    return head

def printlinkedlist(head):
    temp = head
    while temp:
        if temp.next:
            print(temp.data,end=" <-> ")
        else:
            print(temp.data)
        temp = temp.next

l = [1,5,2,4]
num = 0
head = doublelinkedlist(l)
printlinkedlist(head)

new_head = addingNode(head,num)
printlinkedlist(new_head)