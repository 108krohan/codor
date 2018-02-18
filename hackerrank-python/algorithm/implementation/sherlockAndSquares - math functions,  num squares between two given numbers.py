# -*- coding: utf-8 -*-
"""sherlock and squares at hackerrank.com
"""
"""
Both limits inclusive.

Input Format 
The first line contains T, the number of test cases.
T test cases follow, each in a new line. 
Each test case contains two space-separated integers denoting A and B.

Output Format 
For each test case, print the required answer in a new line.

Constraints 
1≤T≤100 
1≤A≤B≤109

Sample Input

2
3 9
17 24

Sample output

2
0
"""
import math
testCases = int(raw_input())
for _ in range( testCases ) :
    low, high = map(int, raw_input().split())
    low, high = low**0.5, high**0.5
    total = 0
    for num in range(int(math.ceil(low)), int(math.floor(high)) + 1) :
        total += 1
    print total
    
