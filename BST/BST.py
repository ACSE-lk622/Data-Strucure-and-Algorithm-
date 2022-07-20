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


newBST = BSTNode(None)
insertNode(newBST,70)
insertNode(newBST,60)
insertNode(newBST,50)
insertNode(newBST,30)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,40)
insertNode(newBST,20)
inOrderTraversal(newBST)