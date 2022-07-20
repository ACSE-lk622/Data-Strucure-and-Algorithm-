from array import *

arr1 = array('i',[1,2,3,4,5,6])


#O(1)
def accessElement(array,index):
    if index >= len(array):
        print('There is not my element in the index')
    else :
        print(array[index])


def searchArray(array, value) : 
    for i in array :
        if i == value :
            return array.index(value)
    return "The element does not exist in this array"
print(searchArray(arr1,6))


#3 append any value to the array 
print('step 3')
arr1.append(7)
print(arr1)

#4 Insert value in an array using insert () method 
print('step 4')
arr1.insert(0,11)
print(arr1)


#5 extend python array using extend() method
print('step 5')
arr2 = array('i',[10,11,12])
arr1.extend(arr2)
print(arr1)

#6 Add item from list into array using fromlist() method 
print('step 6')
tempList = [20,21,22]
arr1.fromlist(tempList)
print(arr1)

#7 remove any array element using remove() method O(N)
print('step 7')
arr1.remove(22)
print(arr1)

#8 remove last array element using pop() method 
print('step 8')
arr1.pop()
print(arr1)

#9 Fetch any element through its index using index() method 
print('step 9')
print(arr1.index(20))

#10 Reverse a python array using reverse() method 
print('step10')
arr1.reverse()
print(arr1)

#11 Get array buffer information through buffer_info() method 
print('step11')
print(arr1.buffer_info())

#12 Check for number of occurences of an element using count() method 
print('step 12 ')
print(arr1.count(11))

#13 Convert array into list with same elements using tolist() method 
print('step 13')
print(arr1.tolist())

#14 Slice elements from an array 
print('step 14 ')
print(arr1[1:4])
print(arr1[3:])
print(arr1[:])