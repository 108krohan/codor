"""Checks if a number is fibonacci or not"""
def fib(x):
    assert type(x) == int and x >= 0
    if x == 0 or x == 1 :
        return 1
    else :
        return fib(x-1) + fib(x-2)

def f(n):
    for i in range(n+1):
        print 'fibonacci of', ' = ', fib(i)

x = int(raw_input("Enter a number of fibonacci terms you want to see\t: "))
print f(x)
