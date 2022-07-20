newTuple = ('a','b','c','d','e')
newTuple1 = ('a',) #Only one element need include comma
newTuple2 = tuple('abcde') #　each character as a separate element , tyuple is the name of constructor
print(newTuple)
print(newTuple2)

print(newTuple[-1])#index
print(newTuple[1])
#slice operator
print(newTuple[1:3])

for i in newTuple:
    print(i)

print(newTuple + newTuple1)
print('a' in newTuple)
print(newTuple.count('a'))
print(newTuple.index('c'))
print(len(newTuple))

print(tuple([1,2,3,4,5,6]))#convert list to tuple

tuple1 = 0,1,2,3,4,5,6
tuple1 = 7,8,9,0 #can not reassign individual element in tuple but can reaasign whole tuple 
print(tuple1)


list1 = [(1,2),(3,4),(5,5)]#create tuple in list 
list1[0] = 3
print(list1)
init_tuple_a = 1, 2
init_tuple_b = (3, 4)
 
[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]

init_tuple = [(0, 1), (1, 2), (2, 3)]
 
print(init_tuple.index(1))
 
