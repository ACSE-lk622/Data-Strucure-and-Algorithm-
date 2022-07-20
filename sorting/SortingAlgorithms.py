from calendar import c
from cmath import sqrt
import math
from winreg import QueryInfoKey

def bubbleSort(customList): #TC :O(N^2) SC : O(1 ) 
    for  i in range(len(customList)-1):
        for j in range(len(customList)-i-1): #need to decrease number of loops which are already compared 
            if customList[j] > customList[j+1]:
                temp = customList[j]
                customList[j] = customList[j+1]
                customList[j+1] = temp 
    print(customList)

def selectionSort(customList): #TC : O(N^2) SC:O(1)
    for i in range(len(customList)):
        min_index = i 
        for j in range(i+1,len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j 
        temp = customList[i]
        customList[i] = customList[min_index]
        customList[min_index] = temp
    print(customList)

def insertionSort(customList):#TC : O(N^2) SC:O(1)
    for i in range(1,len(customList)): #compare current element with next element
        key = customList[i]
        j = i-1 #current element
        while j>=0 and key <customList[j]:
            customList[j+1]= customList[j]
            j-= 1
        customList[j+1] = key
    print(customList)    
def bucketSort(customList):
    numberofBuckets = round(math.sqrt(customList))
    maxValue = len(customList)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j*numberofBuckets/maxValue)
        arr[index_b-1].append(j)
    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i]) # can use best performing sorting algorithm to sort each buckets , in here we use insertSort which is O(N^2)
    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

def merge(customList,l,m,r):
    n1 = m - l + 1
    n2 = r - m 

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0,n1):
        L[i] = customList[l+i]
    
    for j in range(0,n2):
        R[j] = customList[m+1+j]
    i = 0
    j = 0 
    k = l
    while i < n1 and j < n2 :
        if L[i] < R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1 : #當一邊已經先比完剩下的ａｒｒａｙ
        customList[k] = L[i]
        i += 1
        k += 1
    while j < n2 :#當一邊已經先比完剩下的ａｒｒａｙ
        customList[k] = R[j]
        j += 1
        k += 1
def mergeSort(customList, l, r):#TC:O(NlogN), SC :O(N)
    if l < r :
        m = (l+r-1)//2
        mergeSort(customList,l,m)
        mergeSort(customList,m+1,r)#O(NlogN)
        merge(customList,l,m,r) # O(N)
    return customList 
def quickSort(customList,left,right):
    if left > right :
        return 
    L = left
    R = right
    key = customList[right]
    while L != R: 
        while customList[L] < key and L < R :
            L += 1
        while customList[R] >= key and L < R :
            R -= 1
        if L < R :
            customList[L],customList[R] = customList[R], customList[L]
    customList[right] = customList[R]
    customList[R] = key 

    quickSort(customList,left,R-1)
    quickSort(customList,R+1,right)

def heapify(customList,n,i):
    smallest = i 
    l = 2*i + 1
    r = 2*i + 2
    if l < n  and customList[l] < customList[smallest]:
        smallest = l
    if r < n  and customList[r] < customList[smallest]:#This two line code can classify the smallest number in three node 
        smallest = r    
    if smallest != i :
        customList[i] , customList[smallest] = customList[smallest], customList[i]
        heapify(customList,n,smallest)#call recursively to affected subtree

def heapSort(customList):
    n = len(customList)
    for i in range(int(n/2)-1,-1,-1):
        heapify(customList,n,i)
    
    for i in range(n-1,0,-1):
        customList[i],customList[0] = customList[0],customList[i]
        heapify(customList,i,0)
         
cList = [2,1,7,6,5,3,4,9,8]
quickSort(cList,0,len(cList)-1)
print(cList)