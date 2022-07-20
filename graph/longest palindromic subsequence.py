
def LPS(s,start,end):
    if start > end :
        return 0 
    elif start == end : #meet in the middle and should include the character 
        return 1 
    elif s[start] == s[end]: # include both start and end word 
        return 2 + LPS(s,start+1,end-1)
    else:
        op1 = LPS(s,start+1,end)
        op2 = LPS(s,start,end-1)
        return max(op1,op2)



print(LPS("ELRMENMET",0,len("ELRMENMET")-1))

