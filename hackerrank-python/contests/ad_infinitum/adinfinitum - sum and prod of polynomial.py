# -*- coding: utf-8 -*-
"""infinitum12 polynomial and it's roots at hackerrank.com
"""
"""
Problem Statement

You are given a polynomial of degree N described by its coefficients a0,a1,⋯,aN in the following way: 
a0+a1x+a2x2+⋯+aNxN
It is guaranteed that every root of this polynomial is an integer. Some of its roots could be repeated, such as 4−4x+x2 has two roots both equal to 2.

Let's find the sum and the product of all the roots of given polynomial!

Sample Input 
First line contains a single integer N, 
Second line contains N+1 integers separated by space ai for i=0⋯N

Constraints 
1≤N≤20 
−109≤ai≤109, aN≠0

Output Format 
Print two numbers in one line: the first one should be the sum of the roots, the second one should be the product of them.

Sample Input #0

2
4 -4 1
Sample Output #0

4 4
Sample Input #1

1
5 1
Sample Output #1

-5 -5
Explanation 
As we can see in problem statement, sample polynomial #0 has two roots both equal to 2. Therefore, 2+2=4 and 2⋅2=4. 
Now, the second sample has a polynomial 5+x which has only one root −5.
"""
degree = int(raw_input())
terms = map(int, raw_input().split())
if degree == 1 :
    x = -terms[0]/terms[1]
    print x, x
else :
    suma = -terms[degree-1]/terms[degree]
    prod = ((-1)**(degree) )*terms[0]/terms[degree]
    print suma, prod
