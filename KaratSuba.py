# your code goes here
n1 = 222
n2 = 777
from math import log10

def karatsuba(n1, n2):
    l = int(max(round(log10(n1)), round(log10(n2))))

    if (l == 1):
        return n1 * n2

    if l % 2 != 0:
        l -= 1

    a = n1 / 10 ** (l / 2)
    b = n1 % 10 ** (l / 2)
    c = n2 / 10 ** (l / 2)
    d = n2 % 10 ** (l / 2)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)

    abcd = karatsuba(a+b, c+d)
    adPbc = abcd - ac - bd

    return ((10 ** l * ac) + (10 ** (l / 2) * adPbc) + bd)


print karatsuba(n1, n2)

