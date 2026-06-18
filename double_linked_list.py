class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
def doublelinkedlist(l):
    head = Node(l[0])
    temp = head
    prev = None
    
    for i in range(1,len(l)):
        temp.prev = prev
        temp.next = Node(l[i])
        
        prev = temp
        temp = temp.next
    temp.prev = prev
        
    return head

def printlinkedlist(head):
    temp = head
    while temp:
        if not temp.prev and temp.next:
            print(f"({temp.data},{temp.next.data})")
        elif temp.next and temp.prev:
            print(f"({temp.prev.data},{temp.data},{temp.next.data})")
        else:
            print(f"({temp.prev.data},{temp.data})")
        temp = temp.next
        

l = [3,2,6,7,2]
head = doublelinkedlist(l)
printlinkedlist(head)