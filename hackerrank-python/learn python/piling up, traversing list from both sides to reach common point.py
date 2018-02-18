# -*- coding: utf-8 -*-
"""piling up at hackerrank.com

Problem Statement

There is a horizontal row of n cubes. Side length of
each cube from left to right is given. You need
to create a new vertical pile of cubes. The new pile
should be such that if cubei is on cubej then sideLengthj≥sideLengthi.
But at a time, you can only pick either
the leftmost or the rightmost cube only. Print "Yes" if its possible, "
No" otherwise.

Input Format

First line contains a single integer
T, denoting the number of test cases. 
For each testcase, there are 2 lines. 
First line of each test case contains n. 
Second line of each test case contains n space separated
integers, the sideLengths of the cubes in that order.

Constraints 
1≤T≤5 
1≤n≤105 
1≤sideLength<231

Output Format

For each testcase, output a single line containing
a single word, either a "Yes" or a "No".

Sample Input

2
6
4 3 2 1 3 4
3
1 3 2

Sample Output

Yes
No

Explanation

In the first sample, pick in this order: left, right,
left, right, left, right. 
In the second sample no order gives an appropriate
arrangement since 3 will always come after either 1 or 2.
"""
result = []
record = []
try :
    numCases = int(raw_input())
except :
    pass
for _ in range(numCases) :
    oRLen = int(raw_input())
    oneRecord = map(int, raw_input().split())
    left = 0
    right = oRLen - 1
    

    while (oneRecord[left] >= oneRecord[left+1] or \
          oneRecord[right] >= oneRecord[right - 1]) and \
          oneRecord[left] is not oneRecord[right] and \
          left < right:
        if oneRecord[left] >= oneRecord[left+1] :
            left += 1
        if oneRecord[right] >= oneRecord[right - 1] :
            right -= 1
        
    if oneRecord[left] == oneRecord[right] :
        print left, oneRecord[left]
        print right, oneRecord[right]
        result.append('Yes')
    else :
        print left, oneRecord[left]
        print right, oneRecord[right]
        result.append('No')
for i in result :
    print i

""" Shit another Solution :

from collections import deque 
import sys
for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    lst = deque(arr)

    curr = 9999999999999999
    flag = 0
    if (len(lst)<=2):
        print "Yes"
        continue
    left = lst.popleft()
    right = lst.pop()
    latest = -1
    while (len(lst)>0):
        flag = 0
        if (left >= right and left <= curr):
            curr = left
            left = lst.popleft()
            latest = left
            flag = 1
        elif (right> left and right <= curr):
            curr = right
            right = lst.pop()
            latest = right
            flag = 1
        if flag == 0:
            break
    if len(lst)>0 or latest > curr:
        print "No"
    else:
        print "Yes"
"""
