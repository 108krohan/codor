# -*- coding: utf-8 -*-
"""

Problem Statement

You know my methods, Watson.

In elementary schools, while adding two positive integers we start from the right most digit and carry forward the overhead. If there are less digits in one of the numbers, we add leading zeroes to it. For example, for adding 39 and 9, first we add one leading zero to 9.

        carry    1
                 3 9
            +    0 9
                ---------
                 4 8
Now, Watson defines Weird sum as the sum if we ignore carry at each step. For example, Weird sum of 39 and 9 would be 38.

Watson wants Sherlock to generate two numbers A and B such that 1≤A≤N and 1≤B≤M and their weird sum is maximum. Note that A and B can be the same number also.

Input Format

First line contains T, the number of test cases. 
Each test case consists of N and M in one line. None of the number in input has leading zeroes.

Output Format

For each test case, in one line, output the maximum Non-Carry sum possible of two integers A and B such that 1≤A≤N and 1≤B≤M. Output number shouldn't have leading zeroes.

Constraints 
1≤T≤100 
1≤N,M≤1016

Sample Input

2
3 5
16 9
Sample Output

8
19
Explanation

For the first test case, 3 and 5 give a Weird sum of 8.

For second test case, one of the pairs of A and B could be 13 and 6 which gives a maximum possible Weird sum of 19.
"""
####This was all terminated due to timeout!
record = []
numCases = int(raw_input())
for _ in range(numCases) :
    record.append(map(int, raw_input().split()))
result = []

for oneRecord in record :
    a = oneRecord[0]
    b = oneRecord[1]
    oneResult = 0
    for ina in range(1,a+1) :
##        stra = str(ina)
##        stra = stra[::-1]
        for inb in range(1,b+1) :
            tempResult = 0
            inac = ina
            inbc = inb
            while inac > 0 or inbc > 0 :
                tempResult = tempResult*10 + int(str( inac + inbc )[-1])
                inac /= 10
                inbc /= 10
####            print tempResult
            tempResult = int(str(tempResult)[::-1])
##            strb = str(inb)
##            strb = strb[::-1]
##            tempResult = ''
##            bigger = max(len(stra),len(strb))
##            for i in range(bigger) :
##                try :
##                    tempResult += str(int(stra[i]) + int(strb[i]))[-1]
##                except :
##                    if bigger == len(stra) :
##                        tempResult += stra[i]
##                    else :
##                        tempResult += strb[i]
##                        
##            tempResult = tempResult[::-1]
####            print tempResult
##            oneResult = max(int(tempResult), oneResult)
            oneResult = max(tempResult, oneResult)
    result.append(oneResult)
for oneResult1 in result :
    print oneResult1
