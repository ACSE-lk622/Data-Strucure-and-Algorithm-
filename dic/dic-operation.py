myDict = {'one':'uno','two':'dos','three':'tres','four':'cuarto'}

print('one' in myDict) # in only check keys  \ in algorithm use linear search 
print('uno' in myDict.values()) # use value parameter need use values method 

myDict1 = {0:True, 1:False , 2:False}
print(all(myDict1))
print(len(myDict))
myDict2 = {'ererer':1,'aww':2,'uree':3,'orew':4,'i2':5}
print(sorted(myDict2))
print(sorted(myDict2,reverse=True))
print(sorted(myDict2,key=len))#base on length of key to sort

rec = {"Name" : "Python", "Age":"20"}
r = rec.copy()
id1 = id(rec)
id2 = id(r)
print(id1 == id2)
my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4
print(my_dict)