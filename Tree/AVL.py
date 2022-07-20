from turtle import left, right
import queuelinkedlist as queue

class AVLNode:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1 
def preOrderTraversal(rootNode): #O(n) time and space
    if not rootNode:
        return 
    # print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftchild)
    # print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    # print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            # print(root.value.data)
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customQueue.enqueue(root.value.rightchild)  

def searchNode(rootNode,nodeValue): #O(N) time and space
    if rootNode.data == nodeValue:
         print("The value is found")
    elif nodeValue < rootNode.data:
        searchNode(rootNode.leftchild,nodeValue)
    else:
        searchNode(rootNode.rightchild,nodeValue)

def getHeight(rootNode):
    if not rootNode:
        return 0 
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftchild
    disbalanceNode.leftchild = disbalanceNode.leftchild.rightchild
    newRoot.rightchild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftchild),getHeight(disbalanceNode.rightchild)) #add one because add its parent node  
    newRoot.height = 1 + max(getHeight(newRoot.leftchild),getHeight(newRoot.rightchild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightchild
    disbalanceNode.rightchild = disbalanceNode.rightchild.leftchild
    newRoot.leftchild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftchild),getHeight(disbalanceNode.rightchild)) #add one because add its parent node  
    newRoot.height = 1 + max(getHeight(newRoot.leftchild),getHeight(newRoot.rightchild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftchild)-getHeight(rootNode.rightchild)

def insertNode(rootNode,nodeValue):#　O(logn) time and space 
    if not rootNode:#　O(1)
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftchild = insertNode(rootNode.leftchild,nodeValue) #　O(logn)
    else:
         rootNode.rightchild = insertNode(rootNode.rightchild,nodeValue) #　O(logn)
    rootNode.height = 1 + max(getHeight(rootNode.leftchild),getHeight(rootNode.rightchild))#　O(1)
    balance = getBalance(rootNode)#　O(1)
    if balance > 1 and nodeValue < rootNode.leftchild.data:#　O(1)
        return rightRotate(rootNode)#　O(1)
    if balance > 1 and nodeValue > rootNode.leftchild.data:#　O(1)
        rootNode.leftchild = leftRotate(rootNode.leftchild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightchild.data:#　O(1)
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightchild.data:#　O(1)
        rootNode.rightchild = rightRotate(rootNode.rightchild)
        return leftRotate(rootNode)
    return rootNode

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftchild is None:
        return rootNode
    return getMinValueNode(rootNode.leftchild)

def deleteNode(rootNode,nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftchild = deleteNode(rootNode.leftchild,nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.rightchild = deleteNode(rootNode.rightchild,nodeValue)
    else:
        if rootNode.leftchild is None:
            temp = rootNode.rightchild 
            rootNode = None
            return temp
        elif rootNode.rightchild is None:
            temp = rootNode.leftchild 
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightchild)
        rootNode.data = temp.data
        rootNode.rightchild = deleteNode(rootNode.rightchild,temp.data)
    rootNode.height = 1 + max(getHeight(rootNode.leftchild),getHeight(rootNode.rightchild))
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftchild) >= 0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightchild) <= 0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftchild) < 0:
        rootNode.leftchild = leftRotate(rootNode.leftchild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightchild) > 0:
        rootNode.rightchild = rightRotate(rootNode.rightchild)
        return leftRotate(rootNode)

def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftchild = None
    rootNode.rightchild = None
    return "The AVL has been successfully deleted"
newAVL = AVLNode(5)
newAVL = insertNode(newAVL,10)
newAVL = insertNode(newAVL,15)
newAVL = insertNode(newAVL,20)
levelOrderTraversal(newAVL)
