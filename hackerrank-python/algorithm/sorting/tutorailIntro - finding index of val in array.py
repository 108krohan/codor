# -*- coding: utf-8 -*-
"""tutorial intro at hackerrank.com
"""
"""
Input Format 
Given an array, find the index of a value in that array.

There will be three lines of input:

V - the value that has to be searched.
n - the size of the array.
ar - n numbers that make up the array.

Output Format 

Output the index of V in the array.

Constraints

1≤n≤1000
−1000≤V≤1000,V∈ar

Sample Input

4
6
1 4 5 7 9 12

Sample Output

1

Explanation 

V=4. The value 4 is the 2nd element in the array, but its
index is 1 since array indices start from 0, so the answer is 1
"""

val = int(raw_input())
size = int(raw_input())
array = map(int, raw_input().split())
if val in array :
    print array.index(val)
