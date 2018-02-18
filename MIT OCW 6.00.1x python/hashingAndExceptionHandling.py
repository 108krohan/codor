"""Lecture 10 : Hashing and Exception Handling in Python"""

####Hashing in Python
##numBuckets = 50
##
##def create():
##    global numBuckets
##    hSet = []
##    for i in range (numBuckets) :
##        hSet.append([])
##    return hSet
##
##def hashElem(e):
##    global numBuckets
##    return e%numBuckets
##
##def insert(hSet, i):
##    global numBuckets
##    hSet[hashElem(i)].append(i)
##
##def remove(hSet, i):
##    newBucket = []
##    for j in hSet[hashElem(i)]:
##        if j is not i :
##            newBucket.append(j)
##    hSet[hashElem(i)] = newBucket
##
##def member(hSet, i):
##    return i in hSet[hashElem(i)]
##
##def test1():
##    s = create()
##    for i in range(40) :
##        insert(s,i)
##    insert(s,325)
##    insert(s,325)
##    insert(s,43)
##    insert(s,2)
##    print s
##    print member(s, 325)
##    remove (s, 325)
##    print member(s, 325)
##    print member(s, 43)

##Polymorphism and exception handling in python

def readVal(valType, requestMsg, errorMsg):
    numTries = 0
    while numTries < 4 :
        val = raw_input(requestMsg)
        try :
            val = valType(val)
            return val
        except ValueError :
            print(errorMsg)
            numTries += 1
    raise TypeError('Number of tries exceeded')

print readVal(int, "Enter int : ", 'Not an int')

try :
    readVal(int, 'Enter int : ', 'Not an int')
except TypeError,s :
    print s
    
