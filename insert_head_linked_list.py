class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def insert_head_linked_list(head,num):
    temp = head
    head = Node(num,temp)

    return head

def printlinkedlist(head):
    temp = head
    while temp:
        if temp.next:
            print(temp.data,end=" --> ")
        else:
            print(temp.data)
        temp = temp.next
        
def linkedlistconverter(l):
    if l == []:
        return None
    head = Node(l[0])
    temp = head
    n = len(l)
    
    for i in range(1,n):
        temp.next = Node(l[i])
        temp = temp.next
    
    return head
    
if __name__ == "__main__":
    l = eval(input("Enter a list for linked list converstion "))

    head = linkedlistconverter(l)
    printlinkedlist(head)
    
    num = int(input("Enter the number you want to make as the new head "))

    new_head = insert_head_linked_list(head,num)
    printlinkedlist(new_head)