from telnetlib import DO
from xmlrpc.server import DocCGIXMLRPCRequestHandler


class Node :
    def __init__(self,value=None):
        self.value = value 
        self.next = None
        self.prev = None
class DoubleLinkedList :
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head 
        while node :
            yield node 
            node = node.next
    #Creation of double linked list
    def createDLL(self,nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node 
        self.tail = node 
        return "The DLL is created Succes sfully"

    #insertion method in doubly linked list 
    def insertNode(self,nodeValue,location):
        if self.head is None:
            print("The node cannot be inserted")
        else :
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev == None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1 :
                self.tail.next = newNode
                newNode.next = None
                newNode.prev =self.tail
                self.tail = newNode
            else :
                tempNode = self.head
                index = 0 
                while index < location - 1:
                    tempNode = tempNode.nextr
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
    def traverseDLL(self):
        if self.head is None :
            print("There is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    #reverseve traversal method in DLL 
    def reverseTraversalDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
    #search method in DLL
    def searchDLL(self,nodeValue):
        if self.head is None :
            return "There is not any element in the list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does not exsit in the list"
    # delete a node from the DLL
    def deleteNode(self,location):
        if self.head is None :
            print("There is no any element in DLL")
        else:
            if location == 0 :
                if self.head == self.tail :
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1 :
                if self.head == self.tail :
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev 
                    self.tail.next = None
            else:
                tempNode = self.head 
                index = 0 
                while index < location - 1 :
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print("The node has been successfully deleted ")
    # delete all DLL 
    def deleteDLL(self):
        if self.head is None:
            print("There is no node in DLL")
        else:
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted")
doubyLL = DoubleLinkedList()
doubyLL.createDLL(5)
print([node.value for node in doubyLL])
doubyLL.insertNode(0,0)
doubyLL.insertNode(2,-1)
doubyLL.insertNode(3,1)
print([node.value for node in doubyLL])
print(doubyLL.searchDLL(4))
doubyLL.deleteNode(1)
print([node.value for node in doubyLL])
doubyLL.deleteDLL()
print([node.value for node in doubyLL])