def power(base,exp):
    assert exp >= 0 and int(exp) == exp,  'exp has to be a positive and integer number '
    if exp == 0 :
        return 1
    else : 
        return base*power(base,exp-1)

print(power(-2.3,3))