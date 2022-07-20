from tempfile import SpooledTemporaryFile
from unittest.util import _MIN_COMMON_LEN


shoppingList = ['Milk','Cheese','Butter']

for i in shoppingList :
    print(i)

#Update / Insert - List

myList = [1,2,3,4,5,6,7]
myList[2]=33
print(myList)

#List methods insert(),append(),extend()

myList.insert(0,11)
#first position is the position you want to insert,second is the value , Time complexity is O(N)
print(myList)
#Time complexity is O(1) for append
myList.append(55)
print(myList)

# Time complexity for extend is O(N)
newList = [11,12,13,14]
myList.extend(newList)
print(myList)

#Slice operator 

List = ['a','b','c','d','e','f']
print(List[0:2])
List[0:2] = ['x','y']
print(List[:])

#delete method  pop(), del array,remove()

#pop(position),if no position in bracket , it will delete the last one 
#Time complexity will be O(N) if delet not the last one , but will be O(1) if delet last one element
print(List.pop(1))
print(List)

#del method also O(N)
del List[3]
print(List)

#remove(element),time complexity is O(N)
List.remove('d')
print(List)

#Linear search
def searchList(list,value):
    for i in list :
        if i == value :
            print(list.index[value])
    return 'The value does not exist in the list'