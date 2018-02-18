from __future__ import division
import math
import sys
sys.setrecursionlimit(3000)
def facto(n) :
    if n == 1 :
        return 1
    else :
        return n * facto(n - 1)
def fun(n) :
    if n == 1 :
        return 3
    else :
        return n*fun(n - 1) + 3/2
val = 50
##print fun(val), facto(val),
result = fun(val)/facto(val)
##print 3/2
print result
print math.log(result)
##series converges to 4 
##log makes it 1.4
