""" Hackerrank -> Classes : Dealing with Complex Numbers

For this challenge, you are given two complex numbers
and you have to print the result of their addition, subtraction,
multiplication, divison and modulus operations.

:::Input Format:::

Real and imaginary part of a number separated by space.

:::Output Format:::

For two complex numbers C and D, the output should be in the following
sequence
C + D
C - D
C * D
C / D
mod(C)
mod(D)

For complex numbers with non-zero real(A) and complex part(B),
the output should be in the following format :
A + Bi
Replace the plus symbol (+) with a minus symbol (-) when B < 0

For complex numbers with a zero complex part i.e. real numbers,
the output should just be the real number.
For complex numbers where the real part is zero and the complex part(B)
is non-zero, the output should be :
Bi

"""
class complex(object):
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
    def getVal(self):
        self.x, self.y = raw_input().split()
        self.x, self.y = [float(self.x), float(self.y)]
    def __add__(self, other):
        r = other.x + self.x
        i = other.y + self.y
        self.out(i,r)
        
    def __sub__(self, other ):
        r = self.x - other.x 
        i = self.y - other.y
        self.out(i,r)
        
    def __mul__(self, other ):
        r = self.x*other.x - self.y*other.y
        i = self.x*other.y + self.y*other.x
        self.out(i,r)
        
    def __div__(self, other):
        den = (other.x**2 + other.y**2)
        r = (self.x*other.x + self.y*other.y)/den
        i = ( -self.x*other.y + self.y*other.x)/den
        self.out(i,r)
        
    def mod(self):
        self.out( 0, (self.x**2 + self.y**2)**0.5) 
    def out(self,i,r):
        epsilon = .000001
        if abs(i) < epsilon :
            print "{:.2f}".format(r) #7.00
        elif abs(r) < epsilon :
            print "{:.2f}".format(i) + 'i'
        else :
            if i < 0 :
                print "{:.2f}".format(r) + ' - ' + "{:.2f}".format(abs(i)) + 'i'
            else :
                print "{:.2f}".format(r) + ' + ' + "{:.2f}".format(i) + 'i'
        

C = complex()
C.getVal()
D = complex()
D.getVal()
C + D
C - D
C * D
C / D
C.mod()
D.mod() 
