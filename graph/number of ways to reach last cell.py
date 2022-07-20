# 2-D matrx 
# each cell has a cost associated with it for accessing
#start from (0,0) to (n-1,n-1)
#can go down or right 
#find the way it cost minimum

def findmincost(twoArray,row,col,totalcost):
    if totalcost < 0 :
        return 0 
    if row == 0 and col == 0 :
        if twoArray[0][0]-totalcost == 0:
            return 1
        else:
            return 0
    elif row == 0 :
        return findmincost(twoArray,0,col-1,totalcost-twoArray[row][col]) 
    elif col == 0 :
        return findmincost(twoArray,row-1,0,totalcost-twoArray[row][col]) 
    else:
        op1 = findmincost(twoArray,row-1,col,totalcost-twoArray[row][col])
        op2 = findmincost(twoArray,row,col-1,totalcost-twoArray[row][col])
        return op1+op2

twoDlist = [[4,7,1,6],
            [5,7,3,9],
            [3,2,1,2],
            [7,1,6,3],
            ]
print(findmincost(twoDlist,3,3,25))