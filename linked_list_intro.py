class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def printlinkedlist(head,arr):
    temp = head
    for i in range(len(arr)-1):
        print(temp.data,end=" --> ")
        temp = temp.next
    print(temp.data)
    

if __name__ == "__main__":
    arr = [2, 5, 8, 7]
    head = Node(arr[0])
    temp = Node(arr[1])
    head.next = temp
    for i in range(2,len(arr)):
        temp2 = Node(arr[i])
        temp.next = temp2
        temp = temp2
    
    printlinkedlist(head,arr)