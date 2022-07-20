
import queuelinkedlist as queue

class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

def insertNode(rootNode,nodeValue):# O(logN)
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftchild,nodeValue) # O(n/2)
    else:
        if rootNode.rightchild is None:
            rootNode.rightchild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightchild,nodeValue)# O(n/2)
    return "The node has been successfully inserted"
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

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)
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

def minValueNode(bstNode): #find successor 
    current = bstNode
    while(current.leftchild is not None):
        current = current.leftchild
    return current

def deleteNode(rootNode,nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftchild = deleteNode(rootNode.leftchild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightchild = deleteNode(rootNode.rightchild,nodeValue)
    else:
        if rootNode.leftchild is None:
            temp = rootNode.rightchild
            rootNode = None
            return temp
        if rootNode.rightchild is None:
            temp = rootNode.leftchild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightchild)
        rootNode.data = temp.data
        rootNode.rightchild = deleteNode(rootNode.rightchild,temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"
newBST = BSTNode(None)
insertNode(newBST,70)
insertNode(newBST,60)
insertNode(newBST,50)
insertNode(newBST,30)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,40)
insertNode(newBST,20)
searchNode(newBST,50)