def linearSearch(array,value):
    for i in array :
        if i == value :
            return array.index(i)
    return -1 

print(linearSearch([10,20,30,40,50],40))