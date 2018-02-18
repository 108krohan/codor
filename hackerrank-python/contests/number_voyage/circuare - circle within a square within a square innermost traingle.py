from __future__ import division
from math import pi
rad2 = (25*25*5)/(6*6*6)
print rad2
def area(times) :
    if times == 2 :
        return 8 + 1
    else :
        return  1 + 8 * area(times - 1)

print area(2)
result = (4 - 3.14) * rad2 * area(30)

##print area(30)
print result
rate = 864/(20 - 5 * 3.14)
print rate
##rate = 200
cost = result * rate
print cost
##upto = 572**0.5
##print upto
##
##primes = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23]
##for i in primes :
##    if 572 % i == 0 :
##        print i

upto = (cost / 10**18) **.5

print upto
upto = int(upto)
print upto

def isPrime(val) :

    for i in range(2, int(val**.5) + 1) :
        if val%i == 0 :
            return False
    return True 

while True :
    if isPrime(upto) :
        print upto
        break
    upto -= 1
