class Stack :
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    #isempty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #isfull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    #push 
    def push(self,value):
        if self.isFull():
            return "The stack is Full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"
    
    #pop
    def pop(self):
        if self.isEmpty():
            return "There is no any element in the stack"
        else:
            return self.list.pop()
    #peek
    def peek(self):
        if self.isEmpty():
            return "There is no any element in the stack"
        else:
            return self.list[len(self.list)-1]
    #delete
    def delete(self):
        self.list = None
        
customstack = Stack(4)
print(customstack.isEmpty())
print(customstack.isFull())
customstack.push(1)
customstack.push(2)
customstack.push(3)
print(customstack)
