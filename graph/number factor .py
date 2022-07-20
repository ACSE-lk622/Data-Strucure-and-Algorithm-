#number factor 
#for given a N , find number of ways to express N  as provided number 

# divide and conquer
def numberfactor(n):
    if n in (0,1,2):
        return 1 
    elif n == 3:
        return 2 
    elif n == 4 :
        return 4
    else :
        subP1 = numberfactor(n-1)
        subP2 = numberfactor(n-3)
        subP3 = numberfactor(n-4)
        return subP1 + subP2 + subP3
# dynamic programming : top down 
def numberfactor1(n,tempDict):
    if n in (0,1,2):
        return 1 
    if n == 3 :
        return 2 
    else:
        if n not in tempDict:
            subP1 = numberfactor1(n-1,tempDict)
            subP2 = numberfactor1(n-3,tempDict)
            subP3 = numberfactor1(n-4,tempDict)
            tempDict[n] = subP1 + subP2 + subP3
        return tempDict[n]
#dynamic programming : bottom up 
def numberfactor2(n):
    tempArr = [1,1,1,2]
    for i in range(4,n+1):
        tempArr.append(tempArr[i-1]+tempArr[i-3]+tempArr[i-4])
    return tempArr[n]
print(numberfactor(7))