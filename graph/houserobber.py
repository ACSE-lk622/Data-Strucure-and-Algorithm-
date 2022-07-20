#house robber 
#given number of houses , cannot rob adjacent houses and find maximun amouts of money 


#divide and conquer
def houserobber(houses,currentIndex):
    if currentIndex >= len(houses):
        return 0 

    else:
        stealFirsthouse = houses[currentIndex] + houserobber(houses , currentIndex + 2 )
        skipFirsthouse = houserobber(houses , currentIndex + 1)
        return max(stealFirsthouse,skipFirsthouse)

# dynamic programming : top down
def houserobber1(house,currentIndex,Dict):
    if currentIndex >= len(house):
        return 0
    else:
        if currentIndex not in Dict :
            stealFirsthouse = house[currentIndex] + houserobber1(house,currentIndex+2,Dict)
            stealSecondhouse = + houserobber1(house,currentIndex+1,Dict)
            Dict[currentIndex] = max(stealFirsthouse,stealSecondhouse)
        return Dict[currentIndex]
# dynamic programming : down up 
def houserobber2(house,currentIndex):
    tempArr = [0]*(len(house)+2)
    for i in range(len(house)-1,-1,-1):
        tempArr[i] = max(house[i]+tempArr[i+2],tempArr[i+1]) #begin from the last item 
    return tempArr[0] # return the first one 
houses = [6,7,1,30,8,2,4]
print(houserobber(houses,0))