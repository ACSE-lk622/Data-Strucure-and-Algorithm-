

# call the same fib many times , so slow 
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else :
        return fib(n-2)+fib(n-1)  


def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1 :
        return m
    return m + multiply(m,n-1)
def is_prime(n,i=2):
    if n == 2 :
        return True
    if n % i == 0 :
        return False 
    elif i*i > n :
        return True
    else : 
         return is_prime(n,i+1)
def hailstone(n):
    if n == 1 :
        print(n)
        return None
    if n % 2 == 0 :
        print(n)
        return hailstone(n/2)
    else :
        print(n)
        return hailstone(n*3+1)
def merge(n1, n2):
    
    if n1 == 0 :
        return n2 
    if n2 == 0 :
        return n1 
    elif n1 % 10 < n2 % 10 :
        return merge(n1 // 10 ,n2)*10 + n1 % 10 
    else : 
        return merge(n1  ,n2 // 10 )*10 + n2 % 10 