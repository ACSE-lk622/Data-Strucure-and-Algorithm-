

from selectors import EpollSelector


class Node :
    def __init__(self,value = None):
        self.value = value
        self.next = None
class SLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node 
            node = node.next
    def insertSLL(self,value,location):
        newNode = Node(value)
        if self.head is None : #Insert node in the none Linkedlist
            self.head = newNode
            self.tail = newNode
        else :
            if location == 0 :
                newNode.next = self.head # head store original first node location 
                self.head = newNode
            elif location == -1: # insert at the end of Linkedlist
                newNode.next = None
                self.tail.next = newNode #set original last node point to new Node
                self.tail = newNode  # set newnode as tail node 
            else : 
                tempNode = self.head
                index = 0 
                while index < location-1:
                    tempNode =tempNode.next
                    index+=1
                nextNode = tempNode.next # memorized nextnode location first
                tempNode.next = newNode # assign tempNode.next to our newNode
                newNode.next = nextNode # assign newNode.next to previous nextnode location
                if tempNode == self.tail:
                    self.tail = newNode  
    # Traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None :
            print("The Singly Linked List does not exist")
        else :
            node = self.head
            while node is not None :
                print(node.value)
                node = node.next
    def searchSLL(self,nodeValue):
        if self.head is None:
            return "The list does not exist"
        else :
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in the list "
    def deleteNode(self,location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            if location == 0 :
                if self.head == self.tail: #only one node
                    self.head = None 
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1 :
                if self.head == self.tail: #only one node
                    self.head = None 
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0 
                while index < location -1 :
                    tempNode = tempNode.next
                    index += 1 
                nextNode = tempNode.next
                tempNode.next = nextNode.next


            

