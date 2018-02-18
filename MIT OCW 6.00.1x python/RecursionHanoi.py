"""Solving the famous Towers of Hanoi problem,
along with simple cases of recursion"""

####Exponents of a given number. A numeral raised to a certain power.
##def simpleExp (a,x) :
##    if ( x == 1 ) :
##        return a
##    else :
##        return a * simpleExp(a,x-1)
##    
##print simpleExp(2,10)

"""Hanoi Problem Solution"""

def Hanoi (n,f,t,s) :
    if n == 1 :
        print 'move from ' + f + ' to ' + t
    else :
        Hanoi(n-1,f,s,t)
        Hanoi(1,f,t,s)
        Hanoi(n-1,s,t,f)
