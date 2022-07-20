import QueueLinkedList as queue

class AVLNode:
    def __init__(self,data):
        self.data = data 
        self.leftchild = None
        self.rightchild = None
        self.height = 1 

def preOrderTraversal(rootNode): #O(n) time and space
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)