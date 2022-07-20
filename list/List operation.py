a = [1,2,3]
b = [4,5,6]
c = a + b 
print(c)

a = [0]
a = a * 4 
print(a)

# myList = list()
# while(True):
#     inp = input('Enter a number :')
#     if inp == 'done' : break
#     value = float(inp)
#     myList.append(value)
# average = sum(myList)/len(myList)

# print('Average :',average)


a = 'spam'
b = list(a)
print(b)

a = 'spam spam spam'
b = a.split()
print(b)

#convert string to list 
a = 'spam-spam-spam'
delimiter = '-'
b = a.split(delimiter)
print(b)

#rejoin list the string 
print(delimiter.join(b))
a=[1,2,3,4,5]
print(a[3:0:-1])
a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50
print(a)

fruit=['apple', 'banana', 'papaya', 'cherry']

arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list2[0] = 'Guava'
print(fruit_list1)   