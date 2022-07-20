myDict = {'name':'Edy','age':26}

#print(myDict.pop('name'))
#print(myDict.popitem())  return key and value 

#myDict.clear()  clear all dictionary
#del myDict['age']  delete the pair
dict = myDict.copy()
newDict = {}.fromkeys([1,2,3],0) # dictionary.fromkeys(sequence[],value)
#print(myDict.get('age', 27))
#print(myDict.items())
#print(myDict.keys())
#print(myDict.popitem())
#print(dict)
#print(newDict)
print(myDict.setdefault('name','added')) #dictionary.setdefault(key,default_value)
print(myDict.setdefault('name1','added'))
print(myDict)
print(myDict.pop('name2','Edy'))
print(myDict)
print(myDict.values()) # return all value
newDict1 = {'a':1,'b':2,'c':3}
myDict.update(newDict1)
print(myDict)