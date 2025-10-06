class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)        
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        self.head = self.head.next

    def display(self):
        node = self.head
        while node.next:
            print(node.data, end="")
            node = node.next
        print(node.data)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

s.display()
s.pop()

s.display()

        