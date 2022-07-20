
import queuelinkedlist as queue

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
newBT = TreeNode("Drinks")
leftchild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftchild.leftchild = tea
leftchild.rightchild = coffee
rightchild = TreeNode("Cold")
newBT.leftchild = leftchild
newBT.rightchild = rightchild

def preOrderTraversal(rootNode): #O(n) for Time and space complexity 
    if not rootNode:
        return 
    print(rootNode.data) #O(1)
    preOrderTraversal(rootNode.leftchild) #O(n/2)
    preOrderTraversal(rootNode.rightchild) #O(n/2)

def inOrderTraversal(rootNode):#O(n) for Time and space complexity
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftchild)#O(n/2)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)#O(n/2)

def postOrderTraversal(rootNode):#O(n) for Time and space complexity
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftchild)#O(n/2)
    postOrderTraversal(rootNode. rightchild)#O(n/2)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)
def searchBT(rootNode,nodeValue): # O(n) space and time complexity
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)
        return "Not found"

def insertNodeBT(rootNode,newNode): #use level order traversal ,O(n) time complexity , Space complexity is O(n )
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)
            else:
                root.value.leftchild = newNode
                return "Successfully Inserted"
            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)
            else:
                root.value.rightchild = newNode
                return "Successfully Inserted"

def getDeepestNode(rootNode):
    if not rootNode:
        return 
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)
        deepestNode = root.value
        return  deepestNode 

def deleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value == dNode:
                root.value = None
                return 
            if root.value.rightchild:
                if root.value.rightchild is dNode:
                    root.value.rightchild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightchild)
            if root.value.leftchild:
                if root.value.leftchild is dNode:
                    root.value.leftchild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftchild)

def deleteNodeBT(rootNode,node):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode,dNode)
                return "The node has been deleted"
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)
        return "Failed to delete"

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftchild = None
    rootNode.rightchild = None
    return "The BT has been successfully deleted"