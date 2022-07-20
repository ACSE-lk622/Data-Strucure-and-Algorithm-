from ast import Break
from telnetlib import DO
from xmlrpc.server import DocCGIXMLRPCRequestHandler


class Node :
    def __init__(self,value=None):
        self.value = value 
        self.next = None
        self.prev = None
class CircularDoubleLinkedList :
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head 
        while node :
            yield node 
            node = node.next
            if node == self.tail.next: #retrun to the first 
                break
    #Creation of Circular double linked list
    def createCDLL(self,nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode
        return "The CDLL is created successfully"
    # insertion method in circular doubly linked list
    def insertCDLL(self,value,location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0 :
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1 :
                self.tail.next = newNode
                newNode.prev = self.tail
                newNode.next =self.head
                self.head.prev = newNode
                self.tail = newNode
            else :
                tempNode = self.head 
                index = 0 
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next = newNode
                newNode.next.prev = newNode
            return "The node has been successfully inserted"

    #traverse of Circular Doubly Linked List
    def traversalCDLL(self): #O(n) time complexity  O(1) space complexity 
        if self.head is None:
            print("There is no any node for traversal ")
        else :
            tempNode = self.head 
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail :
                    break
                tempNode = tempNode.next
    def reverseTraversalCDLL(self):
        if self.head is None :
            print("There is no any node for reverse traversal")
        else :
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev
    #search Circular Doubly Linked List
    def searchCDLL(self,nodeValue):
        if self.head is None:
            return "There is no any node in CDLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail :
                    return "The value does not exist in CDLL"
                tempNode = tempNode.next
    def deleteNode(self,location):
        if self.head is None :
            print("There is no node to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                    self.head.prev = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1 :
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                    self.head.prev = None
                else:
                    self.tail = self.tail.prev 
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location-1 :
                    index += 1
                    tempNode = tempNode.next
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print("The node has been successfully deleted")
    def deleteCDLL(self):
        if self.head is None:
            print("There is no any node to delete")
        else:
            self.tail.next = None
            tempNode = self.head 
            while tempNode: # delete the reference from other node
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None 
            self.tail = None
            print("The CDLL has been deleted")
        
CircularDLL = CircularDoubleLinkedList()
print(CircularDLL.createCDLL(5))
CircularDLL.insertCDLL(0,0)
CircularDLL.insertCDLL(1,-1)
CircularDLL.insertCDLL(2,2)
print([node.value for node in CircularDLL])
CircularDLL.traversalCDLL()
CircularDLL.deleteNode(-1)
print([node.value for node in CircularDLL])