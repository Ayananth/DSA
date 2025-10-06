class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        node = Node(data)
        if self.rear is None:
            # If queue is empty
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            # Queue became empty
            self.rear = None
        return temp.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
