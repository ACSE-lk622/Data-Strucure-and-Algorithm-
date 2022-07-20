# 2-D matrx 
# each cell has a cost associated with it for accessing
#start from (0,0) to (n-1,n-1)
#can go down or right 
#find the way it cost minimum

def findmincost(twoArray,row,col):
    if row == -1 or col == -1 :
        return float('inf')
    elif row == 0 and col == 0 :
        return  twoArray[0][0]
    else :
        op1 = twoArray[row][col] + findmincost(twoArray,row-1,col)
        op2 = twoArray[row][col] + findmincost(twoArray,row,col-1)
        return min(op1,op2)

twoDlist = [[4,7,8,6,4],
            [6,7,3,9,2],
            [3,8,1,2,4],
            [7,1,7,3,7],
            [2,9,8,9,3],
            ]
print(findmincost(twoDlist,4,4))