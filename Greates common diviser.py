#Euclidean algorithm  gcd(48,18) step 1 : 48/18 = 2 remainder 12 step 2: 18/12 = 1 remainder 6 step 3 : 12/6 = 2 remainder 0


def gcd(a,b):
    assert int(a) == a and int(b) == b,'The number must be integer only ' 
    # the number has to be integer and need convert negative into positive 
    if a < 0 :
        a = -1s*a
    if b < 0 :
        b = -1*b
    if a%b == 0 :
        return b  
    else :
        return gcd(b,a%b)
print(gcd(-36,18))
    