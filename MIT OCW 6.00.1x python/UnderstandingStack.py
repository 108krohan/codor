def f():
    x = 3
    def g():
        x = 'abc'
        print 'x in g = ', x
    x = x + 1
    print 'x = ', x
    g()
##    assert False
    return x
z = 2
x = f()
