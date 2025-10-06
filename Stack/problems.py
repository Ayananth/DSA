# reverse a string using stack
'''s = "Hello"

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack) >= 1
    
stack = Stack()
for i in s:
    stack.push(i)

new_s = ""

while stack.isEmpty():
    new_s += stack.pop()

print(new_s)'''



#implement FIFO using stack ( queue using 2 stacks)
# https://leetcode.com/problems/implement-queue-using-stacks/


'''
class Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = [] 
    def push(self, data):
        self.stack1.append(data)
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:return
        return self.stack2.pop()
'''







