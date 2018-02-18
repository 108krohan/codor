"""testing to see if variable inside a function can be called by another
function"""

def fn() :
    global lite
    print lite

def litr() :
    lite = 'fun'
    fn()
##lite = 'nofun'
litr()
