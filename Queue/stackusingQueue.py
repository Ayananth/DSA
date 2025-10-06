'''
here I am using 2 queues and it is a costly pop operation. (ref: Geeksforgeeeks)
push is normal operation
while pop,
if q1 is empty -> underflow
keep only one elem in q1, transfer all other elems to q2 by popin from q1.
the one elem in q1 is the one we should return to the user.

finally, swap q1 and q2. 

'''


class Queue:
    def __init__(self):
        self.q1 = []
        self.q2 = []
    
    def enqueue(self, data):
        self.q1.append(data)

    def dequeue(self):
        if not self.q1:
            return
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        popped = self.q1.pop()

        self.q1, self.q2 = self.q2, self.q1
        return popped