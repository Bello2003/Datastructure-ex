class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = CNode(data)
        if not self.head:
            self.head = new
            new.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new
            new.next = self.head

    def traverse(self):
        temp = self.head
        if not temp: return
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break

cll = CircularLinkedList()
cll.insert(1)
cll.insert(2)
cll.insert(3)
cll.traverse()
