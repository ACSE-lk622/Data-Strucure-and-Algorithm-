class Heap:
    def __init__(self,size):
        self.customList = (size+1)*[None]
        self.heapSize = 0 
        self.maxSize = size + 1 #not use zero cell

def peekofHeap(rootNode): #space and time complexity is O(1)
    if not rootNode:
        return 
    else:
        return rootNode.customList[1]

def sizeoffHeap(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.heapSize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        for i in range(1,rootNode.heapSize+1): # O(n)
            print(rootNode.customList[i])

def heapifyTreeInsert(rootNode,index,heapType): #time  #O(logN) ,space #O(logN) (calling stack memory)
    parentIndex  = int(index/2)
    if index <= 1:
        return 
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            tmp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = tmp
        heapifyTreeInsert(rootNode,parentIndex,heapType) #recursively check upper node whether meet the critiria of heaptype  O(logN)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            tmp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = tmp
        heapifyTreeInsert(rootNode,parentIndex,heapType) #O(logN)
def insertNode(rootNode,nodeValue,heapType):# O(logn)
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The bnary heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode,rootNode.heapSize,heapType) # O(logn)
    return "The value has been successfully inserted"
def heapifyTreeExtract(rootNode,index,heapType):
    leftIndex = index * 2 
    rightIndex = index * 2 + 1
    swapchild = 0 
    if rootNode.heapSize < leftIndex : #no child  
        return 
    elif rootNode.heapSize == leftIndex: # only left child 
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return 
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp         
            return    
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapchild = leftIndex
            else :
                swapchild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapchild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapchild]
                rootNode.customList[swapchild] = temp  
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapchild = leftIndex
            else :
                swapchild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapchild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapchild]
                rootNode.customList[swapchild] = temp         
        heapifyTreeExtract(rootNode,swapchild,heapType)     
def extractNode(rootNode,heapType): #O(logN)
    if rootNode.heapSize == 0 :
        return 
    else:
         extraxtedNode = rootNode.customList[1]
         rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
         rootNode.customList[rootNode.heapSize] = None
         rootNode.heapSize -= 1
         heapifyTreeExtract(rootNode,1,heapType) #O(logN)
         return extraxtedNode
def deleteEntireBP(rootNode):
    rootNode.customList = None
newHeap = Heap(5)
insertNode(newHeap,4,"Max")
insertNode(newHeap,5,"Max")
insertNode(newHeap,2,"Max")
insertNode(newHeap,1,"Max")
extractNode(newHeap,"Min")
levelOrderTraversal(newHeap)