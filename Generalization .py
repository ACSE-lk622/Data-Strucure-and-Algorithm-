"""Generalization"""

"""Higher order function""" 
from math import pi,sqrt
from operator import mul

def area(r,shape_constant):
    """ To prevent negative number """
    assert r > 0,'A length must be positve'
    return r*r*shape_constant

def area_square(r):
    return area(r,1)
def area_circle(r):
    return area(r,pi)
def area_hexagon(r):
    return area(r,3*sqrt(3)/2)



def indentity(k):
    return k
def cube(k):
    return pow(k,3)
def summation(n, term):
    """Sum the first N terms of a sequence.
    >>> summation (5,cube)
    225
    """
    total, k = 0, 1
    while k <= n :
        total, k = total +term(k), k + 1
    return total

def sum_naturals(n):
    """SuM the first N natural numbers
    >>> sum_naturals(5)
    15
    """
    return summation(n,indentity)
def sum_cubes(n):
    """Sum  the first N cubes of natural numbers.
    >>> sum_cubes(5)
    225
    """
    return summation(n,cube)
def pi_term(k):
    return  8 / mul(4*k-3,4*k-1)


""" another example"""

def make_adder(n):
    """Return a function that takes 
    K and return K+N.
    >>> add_three = make_adder(3)
    >>> make_adder(3)(4)
    7
    """
    def adder(k):
        return k+n
    return adder 
def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x
def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x
def case_in_point():
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x


def remove (n,digit):
    kept,digits = 0,0
    while n > 0 :
        n = n // 10 
        last = n % 10  
        if last != digit :
            kept = kept +last*10**digits
            digits +=1
    return kept
