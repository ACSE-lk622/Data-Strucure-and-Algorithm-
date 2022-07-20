def insert_sort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i-1 
        while j >= 0 and key < a[j]:
            a[j+1]= a[j]
            j-=1

        a[j+1]= key 
    return a 

def factorial(n):
    assert  n > 0 and int(n) == n,'The number must be positive integer only!'
    if n in [0,1] :
        return 1 
    return n*factorial(n-1) 

def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Fibonacci number cannot be negatove or non integer'
    if n in [0,1]:
        return n 
    else :
        return fibonacci(n-1) + fibonacci(n-2)