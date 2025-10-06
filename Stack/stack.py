class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def display(self):
        print(f"Bottom ---> Up: {self.stack}")

    

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

s.display()
s.pop()

s.display()