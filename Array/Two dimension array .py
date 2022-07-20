
import numpy as np

twoDArray  = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)

newTwoDArray = np.insert(twoDArray, 0 , [[1,2,3,4]],axis=1 )
# axis = 0 will be row , axis = 1 will be column
#0 is number of row or column
print(newTwoDArray)

newTwoDArray = np.append(twoDArray, [[1,2,3,4]],axis=0)
print(newTwoDArray)
print(len(newTwoDArray[0]))
#append only put in the last of array 

def accessElements(array,rowIndex,colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')
    else : 
        print(array[rowIndex][colIndex])

#Traverse Two dimension array

def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])) :
            print(array[i][j])

traverseTDArray(twoDArray)

newTDArray = np.delete(twoDArray, 0 , axis = 0)
print(newTDArray)