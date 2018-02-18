# -*- coding: utf-8 -*-
"""Maximizing XOR at hackerrank.com
"""
"""
Problem Statement

Given two integers, L and R, find the maximal value of A xor B, where A and B satisfy the following condition:

L≤A≤B≤R
Input Format

The input contains two lines; L is present in the first line and R in the second line.

Constraints 
1≤L≤R≤103

Output Format

The maximal value as mentioned in the problem statement.

Sample Input

10
15
Sample Output

7
"""

def maxXor(L, R) :
    result = 0
    for A in range(L, R) :
        for B in range(A, R+1) :
            if A^B > result :
                result = A^B
    return result



L = int(raw_input())
R = int(raw_input())
result = maxXor(L, R)
print result 

