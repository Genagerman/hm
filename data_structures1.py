
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def __str__(self):
        return str(data)

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
    def append(self, data):
        node = Node(data)
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = node
            
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')
current = words.tail
while current:
    print(current.data)
    current = current.next

