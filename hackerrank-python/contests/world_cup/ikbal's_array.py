"""ikbal's array at hackerrank.com
"""
##small = 
num = 1000000007
##def calmod(result) :    
##    result = str(result) 
##    new_res = 0
##    indice = 0
##    exp = 9
##    while result != '' :
##        if len(result) < exp :
##            new_res = (int(result[indice:]) + new_res*10*len(result) - 1) % num
##            result = ''
##        else :
##            new_res = (int(result[indice:indice + exp]) + new_res * (10**exp)) % num
##            result = result[indice + exp:]
##        print new_res, result
##    print result

def add(arr, line) :

    fr, to, kitna = line[1] - 1, line[2], line[3]
    for index in xrange(fr, to) :
        arr[index] += kitna

def final(line) :
    global a, b
    fr, to = line[1] - 1, line[2]
    result = 0
    for index in xrange(fr, to) :
        result += a[index] * b[index]
    if result < 1000000007 :
        print result
    else : 
        print result % 1000000007
    
size, q = map(int, raw_input().split())

a = [0]*size
b = [0]*size
for _ in xrange(q) :

    line = map(int, raw_input().split())

    if line[0] == 1 :
        add(a, line)
##        print a, b
    elif line[0] == 2 :
        add(b, line)
##        print a, b
    else :
        final(line)
        

##def add(arr, aop) :
##    global size
##    index = -1 
##    while index < size :
##        index += 1
##        arr
##size, q = map(int, raw_input().split())
##
##a = [0]*size
##b = [0]*size
##aop = []
##bop = []
##
##for _ in xrange(q) :
##    line = map(int, raw_input().split())
##    if line[0] == 1 :
##        aop.append(line[1:])
##    elif line[1] == 2 :
##        bop.append(line[1:])
##    else :
##        add(a, aop)
##        add(b, bop)
##        final(a, b, line)
##        aop = []
##        bop = []
