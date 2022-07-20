
from turtle import circle


class Node :
    def __init__(self,value = None):
        self.value = value
        self.next = None
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node 
            if node.next == self.head :
                break
            node = node.next
    def createCSLL(self,nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node 
        self.tail = node 
        return "The CSLL has been created "
    
    # Insert of a node in circular singly linked list

    def insertCSLL(self,value,location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0 :
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1 :
                newNode.next = self.tail.next # point to first node 
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0 
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next 
                newNode.next = nextNode
                tempNode.next = newNode
            return "The node has been successfully inserted"
    # tranversal of a node in circular singly linked list
    def traversalCSLL(self): #  Time complexity :O(n) , Space :O(1)
        if self.head is None:
            print("There is no any element for traversal")
        else :
            tempNode = self.head
            while tempNode:
                print(tempNode.value,end = " ")
                tempNode = tempNode.next
                if tempNode == self.tail.next: #reach the end of linked list 
                    break
    def searchCSLL(self,value):
        if self.head is None:
            return "There is no any node in this CSLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value :
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next: #reach the end of linked list 
                    return "The node does not exist in the CSLL"
    #delete a node from circular singly linked list 
    def deleteNode(self,location):
        if self.head is None:
            print("There is no any node in CSLL")
        else :
            if location == 0 :
                if self.head == self.tail :# means only one node
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else :
                    self.head = self.head.next #　access second node 
                    self.tail.next = self.head # tail point ot second node 
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else :
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next 
                    node.next = self.head 
                    self.tail = node 
            else :
                tempNode = self.head
                index = 0 
                while index < location - 1 :
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    
    #delete entire circular singly linked list 
    def deleteEntireCSLL(self):
        self.head = None
        self.tail = None
        self.tail.next = None


circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,-1)
circularSLL.insertCSLL(5,-1)
circularSLL.insertCSLL(4,3)

circularSLL.deleteNode(3)
circularSLL.traversalCSLL()