#　Recursive decomposition : 1 finding simpler instances of the problem 
# explore two possibilities 1 . Use at least one 4  / dont use 4 
def count_partitions(n,m):
    if n == 0:
        return 1 
    elif n < 0 :
        return 0
    elif m <= 0 :
        return 0
    else :
        with_m = count_partitions(n-m,m)
        without_m = count_partitions(n,m-1)
        return with_m + without_m

