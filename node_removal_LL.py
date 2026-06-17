class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def node_removal_LL(l,node):
    if l == []:
        return None
    head = Node(l[0])
    temp = head
    n = len(l)
    
    for i in range(1,n):
        if l[i] == node:
            continue
        temp.next = Node(l[i])
        temp = temp.next
    
    return head
    
l = [4,5,1,9]
node = 5
head = node_removal_LL(l,node)
l = []
temp = head
while temp:
    l.append(temp.data)
    temp = temp.next
    
print(l)