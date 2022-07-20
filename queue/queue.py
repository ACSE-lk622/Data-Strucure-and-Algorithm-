class Queue:
    def __init__(self):
        self.item = []

    def __str__(self):
        values = [str(x) for x in self.item]
        return ' '.join(values)

    def isEmpty(self):
        if self.item == []:
            return True
        else:
            return False
    def enqueue(self,value): #time complexity : O(n),add first element ,other element need to shift setp right ,space is O(1)
        self.item.append(value)
        return "The element is inserted at the end of Queue"
    def dequeue(self): # time complexity : O(n), after remove first element , the last element need to shift one step left, Space is O(1) 
        if self.isEmpty() :
            return "There is no element in this Queue"
        else:
            return self.item.pop(0)  # if call pop without parameter ,will remove last element , if with will remove first element
    def peek(self):
        if self.isEmpty():
            return " There is no element in the Queue"
        else:
            return self.item[0]
    
    def delete(self):
        self.item = []


customqueue = Queue()
print(customqueue.isEmpty())
customqueue.enqueue(1)
customqueue.enqueue(2)
customqueue.enqueue(3)
print(customqueue.dequeue())
print(customqueue)
print(customqueue.peek())
customqueue.delete()
print(customqueue)