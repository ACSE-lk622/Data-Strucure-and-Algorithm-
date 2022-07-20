class item:
    def __init__(self,weight,value,):
        self.weight =weight 
        self.value = value
        self.ratio = value / weight

def knapsackMethod(items,capacity):
    items.sort(key=lambda x: x.ratio,reverse = True) #O(NlogN)
    usedCapacity = 0
    totalvalue = 0 
    for i in items : #O(N)
        if usedCapacity + i.weight <= capacity :
            usedCapacity += i.weight
            totalvalue += i.value 
        else:
            unusedweight = capacity - usedCapacity
            value = i.ratio * unusedweight #sum the protion of weight 
            usedCapacity += unusedweight
            totalvalue += value 
        
        if usedCapacity == capacity :
            break 
    print("Total value obtained: " + str(int(totalvalue)))

item1 = item(20,100)
item2 = item(30,120)
item3 = item(10,60)
cList = [item1,item2,item3]
knapsackMethod(cList,50)