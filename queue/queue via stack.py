class Stack():
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)
    def push(self,item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()

class QueueviaStack():
    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()
    
    def enqueue(self,item):
        self.instack.push(item)

    def dequeue(self):
        while len(self.instack):
            self.outstack.push(self.instack.pop())
        result = self.outstack.pop()
        while len(self.outstack):
            self.instack.push(self.outstack.pop())
        return result 

customQueue = QueueviaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
customQueue.enqueue(4)
print(customQueue.dequeue())