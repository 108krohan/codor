"""Lecture 11 : OOP and Inheritence
A better way to do the hashes"""

class intSet(object):
    #An intset is a set of integers

    def __init__(self):
        """Special status in Python.
        Upon creation of an object, this is executed on that object."""
        """Create an empty set of integers"""
        self.numBuckets = 47
        self.vals = []
        for i in range(self.numBuckets):
            self.vals.append([])

    def hashE(self, e):
        #Private function should not be used inside class
        return abs(e)%len(self.vals)

    def insert(self, e):
        """Assume e is an integer and inserts e into self"""
        for i in self.vals[self.hashE(e)]:
            if i == e : return
        self.vals[self.hashE(e)].append(e)

    def member(self, e):
        """Assume e is an integer and returns True if it's in the hash self"""
        return e in self.vals[self.hashE(e)]

    def __str__(self):
        """Returns string representation of self"""
        elems = []
        for bucket in self.vals :
            for e in bucket :
                elems.append(e)
        elems.sort()
        result = ''
        for e in elems :
            result = result + str(e) + ' '
        return '(' + result[:-1] + ')'

def test1():
    s = intSet()
    for i in range (40):
        s.insert(i)
    print s.member(14)
    print s.member(41)
    print s         #print automatically invokes the function __str__
    print s.vals    #Evil Python will let me do it but I shouldn't do it.
    
