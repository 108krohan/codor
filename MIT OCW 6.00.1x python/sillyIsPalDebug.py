###debugging a code

def isPal(x):
    assert type(x) == list
    ##temp  = x is wrong
    temp = x[:] ##aliasing
    temp.reverse() ##remember to add the parens after the method call
    if temp == x :
        return True
    else :
        return False

def silly(n):
    assert type(n) == int and n > 0
    result = [] ##know the right place to initialise an identifier
    for i in range(n):
        elem = raw_input ("Enter something  ")
        result.append(elem)
    if isPal(result) :
        print 'Is a Palindrome.'
    else :
        print 'Is not a Palindrome.'

def isPalTest():
    L = [1,2]
    result = isPal(L)
    print 'Should print False ', result
    L = [1,2,1]
    result = isPal(L)
    print 'Should print True ', result

isPalTest()
x = int (raw_input("Enter the number of items in the list\t: "))
silly(x)
