
from types import new_class


class BinaryTree:
    def __init__(self,size):
        self.customList =  size*[None]
        self.lastUsedIndex = 0
        self.maxsize = size 
    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxsize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    def searchNode(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not found"
    def preOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    def inOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return 
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.preOrderTraversal(index*2 + 1)

    def postOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)
        print(self.customList[index])


    def levelOrderTraversal(self,index): #O(n)
        for i in range(index,self.lastUsedIndex+1):
            print(self.customList[i])
    
    def deleteNode(self,value): #O(n) time complexity , O(1) space complexity
        if self.lastUsedIndex == 0:
            return "There is no any node to delete"
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"

    def deleteBT(self):
        self.customList = None
        return "The BT has been successfully deleted"
newBT = BinaryTree(8)
print(newBT.insertNode("Drink"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffee"))
newBT.deleteNode("Hot")
newBT.levelOrderTraversal(1)