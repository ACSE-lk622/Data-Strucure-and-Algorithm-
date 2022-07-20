from calendar import c
from sre_constants import SRE_FLAG_IGNORECASE


class Queue:
    def __init__(self,maxsize): #time complexity is O(1),space is O(n)
        self.item = maxsize*[None]
        self.maxsize = maxsize
        self.top = -1 
        self.start = -1 

    def __str__(self):
        values = [str(x) for x in self.item]
        return ' '.join(values)

    def isFull(self):
        if self.top + 1 == self.start :
            return True
        elif self.start == 0 and self.top + 1 == self.maxsize :
            return True
        else:
            return False 
    def isEmpty(self):
        if self.top == -1 :
            return True
        else:
            return False
    def enqueue(self,value): #space and time complexity is O(1)
        if self.isFull():
            return "The queue is full"
        else:       
            if self.top + 1 == self.maxsize:
                self.top = 0 
            else:
                self.top += 1
                if self.start == -1 : # origin no element
                    self.start = 0 
            self.item[self.top] = value
            return "The element is inserted at the end of Queue"
        return "The element is inserted at the end of Queue"
    def dequeue(self): #space and time complexity is O(1)
        if self.isEmpty() :
            return "There is no element in this Queue"
        else:
            firstelement = self.item[self.start]
            start = self.start 
            if self.start == self.top : #only one element
                self.start = -1     
                self.top = -1 
            elif self.start + 1 == self.maxsize: #　back to first element
                self.start = 0 
            else :
                self.start += 1
            self.item[start] = None
            return firstelement
            
    def peek(self):
        if self.isEmpty():
            return " There is no element in the Queue"
        else:
            return self.item[self.start]
    
    def delete(self):
        self.item = self.maxsize * [None]  
        self.top = -1 
        self.start = -1


customqueue = Queue(3)
print(customqueue.isEmpty())
customqueue.enqueue(1)
customqueue.enqueue(2)
customqueue.enqueue(3)
print(customqueue.dequeue())
print(customqueue.peek())
customqueue.delete()
print(customqueue)