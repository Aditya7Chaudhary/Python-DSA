class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def linkedlist(l,pos):
    head = Node(l[0])
    temp = head
    
    count = 0
    for i in range(1,len(l)):
        if count == pos:
            temp2 = temp
        temp.next = Node(l[i])
        temp = temp.next
        count += 1
    temp.next = temp2

    return head

def lengthlinkedlistloop(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            length = 1
            fast = fast.next
            while slow != fast:
                fast = fast.next
                length += 1
            return length
    
    return None

l = [2,5,3,6,3]
pos = 1
head = linkedlist(l,pos)
print(lengthlinkedlistloop(head))