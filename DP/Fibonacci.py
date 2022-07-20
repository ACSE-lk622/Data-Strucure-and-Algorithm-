# top down memorization method => seperate original problem into sub problem ,then merge to original problem

def FibonacciMemorize(n,memo): # TC: O(n) SC : o(n) 
    if n == 1 :
        return 0
    if n == 2 :
        return 1 
    if n not in memo:
        memo[n] = FibonacciMemorize(n-1,memo) + FibonacciMemorize(n-2,memo)
    return memo[n]


def FibonacciTabulation(n): # TC: O(n) SC : o(n) 　avoid recursion 
    tb = [0,1]
    for i in range(2,n+1):
        tb.append(tb[n-1]+tb[n-2])
    return tb[n-1]

mydic = {}

print(FibonacciMemorize(3,mydic))