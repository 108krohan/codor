"""class 2 find the torsional angle at hackerrank.com

Problem Statement

You are given four cords A, B, C and D in the 3-dimensional
cartesian coordinate system. You are required to print
the angle between the plane made by cords A, B, C and B,
C, D in degrees(NOT RADIAN). Let the angle be PHI.
Cos(PHI) = (X . Y)/|X||Y| where X = AB x BC and
Y = BC x CD. Here X.Y mean dot product between X and Y.
AB x BC mean cross product between line segment AB and BC.
AB = B - A.

Input Format

X, Y and Z coordinates of a cord in one line separated by space,
where they are floating numbers.

Output Format

Angle with precision of two digits after decimal.

Sample Input

0 4 5
1 7 6
0 5 9
1 7 2

Sample Output

8.19

"""
import math

class cord(object) :

##    def __init__(self, x = 0.0, y = 0.0, z = 0.0) :
    def __init__(self, default = (0.0, 0.0, 0.0)) :
        self.x = float(default[0])
        self.y = float(default[1])
        self.z = float(default[2])

##    def getVal(self) :
##        self.x, self.y, self.z = map(float, raw_input().split())
##    def cos
    def cross(self, other) :
        new = cord()
        new.x = self.y*other.z - self.z*other.y
        new.y = self.z*other.x - self.x*other.z
        new.z = self.x*other.y - self.y*other.x
        return new

    def segment(self, other) :
        new = cord()
        new.x = other.x - self.x
        new.y = other.y - self.y
        new.z = other.z - self.z
        return new

    def dotProd(self, other) :
        return self.x*other.x + self.y*other.y + self.z*other.z

    def mod(self) :
        return (self.x**2 + self.y**2 + self.z**2)**.5

        
    
A = cord(map(float, raw_input().split()))
##A.getVal()
B = cord(map(float, raw_input().split()))
##B.getVal()
C = cord(map(float, raw_input().split()))
##C.getVal()
D = cord(map(float, raw_input().split()))
##D.getVal()

AB = A.segment(B)
CD = C.segment(D)
BC = B.segment(C)
X = AB.cross(BC)
Y = BC.cross(CD)

nume = X.dotProd(Y)
denom = X.mod()*Y.mod()
##print nume
##print denom
print "{:.02f}".format(math.degrees(math.acos(nume/denom)))
