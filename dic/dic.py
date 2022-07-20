#Create a dictionary
myDict = dict()
print(myDict)

secondDict = {}
print(secondDict)

myDict = {'name':'Edy','age':26}
myDict['age'] = 27  # Time complexity is O(1)
print(myDict)
myDict['address'] = 'London' # Time complexity O(1) Space complexity is amortized O(1)
print(myDict) 

#traverse dictionary
def traverseDict(dict):
    for key in dict:
        print(key,dict[key])

traverseDict(myDict)