"""find point at hackerrank.com
"""

testcases = int(raw_input())
for _ in range(testcases) :
    p_x, p_y, q_x, q_y = [int(i) for i in raw_input().split()]
##    print p_x
    sym_x, sym_y = 2*q_x - p_x, 2*q_y - p_y
    print sym_x, sym_y
"""
Problem Statement

Given two points P and Q, output the symmetric point of point P about Q.

Input format: 
The first line contains an integer T representing the number of testcases (T <= 15) 
Each test case contains Px Py Qx Qy representing the (x,y) coordinates of P and Q, all of them being integers.

Constraints 
1 <= T <= 15 
-100 <= x, y <= 100

Output format 
For each test case output x and y coordinates of the symmetric point (each point in a new line).

Sample input

1  
0 0 1 1
Sample output

2 2
"""
