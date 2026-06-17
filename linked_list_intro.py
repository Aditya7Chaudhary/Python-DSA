class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
        
if __name__ == "__main__":
    arr = [2, 5, 8, 7]
    y = Node(arr[0],0,2)

    print(y)
    print(y.prev,y.data,y.next)