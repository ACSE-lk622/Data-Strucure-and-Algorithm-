class item:
    def __init__(self,profit,weight,):
        self.weight = weight 
        self.profit = profit
def knapsackMethod(items,capacity,currentIndex):
    if currentIndex < 0 or capacity <= 0 or currentIndex >= len(items):
        return 0 
    elif items[currentIndex].weight <= capacity :
        profit1 = items[currentIndex].profit + knapsackMethod(items,capacity-items[currentIndex].weight,currentIndex+1) # choose first element
        profit2 = knapsackMethod(items,capacity,currentIndex+1)
        return max(profit1,profit2)
    else:
        return 0 
mango = item(31,3)
apple = item(26,1)
orange = item(17,2)
banana = item(72,5)
items = [mango,apple,orange,banana]

print(knapsackMethod(items,7,0))