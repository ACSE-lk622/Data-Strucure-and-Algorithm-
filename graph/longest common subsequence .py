


def findLCS(s1,s2,index1,index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0 

    if s1[index1] == s2[index2]:
        return 1 + findLCS(s1,s2,index1+1,index2+1)
    else:# no same character , so there are two options , first one, move s1[index] to s1[index+1] , second move s2[index] to s2[index]
        # s1 = abc  s2 = bcd  => s1[1]-> s2[0], s1[0]->s2[1]
        op1 = findLCS(s1,s2,index1+1,index2)
        op2 = findLCS(s1,s2,index1,index2+1)
        return max(op1,op2) # return max number of same characters  

print(findLCS("elephant","element",0,0))