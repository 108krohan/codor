"""rectangle at number voyage at hackerrank.com
"""
##purely arithmetic
"""
equations that lead to answer :
1. len + br = 32
2. area(triangle) = 1/2 * len * b
3. the area ratio given in question abcd/fbec = 31

method :
1. express 3 as len*br/(len*(br - b)) = 31, express br in terms of b
2. using expr 1, express len in terms of b
3. maximize area in 2 by diff 2 wrt b, this is your b
4. put b in br, then get len via expr 1. Now it's done.
5. multiply len*br

len = 16
br = 16

"""

"""

Problem Statement

Professor Math has a rectangle ABCD, and the perimeter of
the rectangle is 64 kms.Professor Math draws a
line EF parallel to AD, such that Area of ABCDArea of FBCE=31.
He observes that drawing the line EF maximizes the
area of Triangle ADE. Find the area of the Rectangle ABCD.

"""
