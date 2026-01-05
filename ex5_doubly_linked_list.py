class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        new.next = self.head
        if self.head:
            self.head.prev = new
        self.head = new

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

dll = DoublyLinkedList()
dll.insert(10)
dll.insert(20)
dll.traverse()
