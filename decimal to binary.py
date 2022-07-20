def decimalToBinary(n):
    assert int(n) == n, 'The parameter must be an integer only '
    if n == 0 :
        return 0
    else :
        return n%10 + 10*decimalToBinary(n/2)