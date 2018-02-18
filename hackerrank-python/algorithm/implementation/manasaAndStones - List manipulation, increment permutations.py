"""Manasa and Stones at hackerrank.com

Problem Statement

Manasa is out on a hike with friends. She finds a trail of stones
with numbers on them. She starts following the trail and notices that
two consecutive stones have a difference of either a or b.
Legend has it that there is a treasure trove at the end of the trail
and if Manasa can guess the value of the last stone,
the treasure would be hers.
Given that the number on the first stone was 0, find
all the possible values for the number on the last stone.

Note: The numbers on the stones are in increasing order.

:::Input Format:::

The first line contains an integer T, i.e. the number of test cases.
T test cases follow; each has 3 lines.
The first line contains n (the number of stones).
The second line contains a, and the third line contains b.

:::Output Format:::

Space-separated list of numbers which are the possible
values of the last stone in increasing order.

Sample Input

2
3 
1
2
4
10
100

Sample Output

2 3 4 
30 120 210 300 

Explanation

All possible series for the first test case are given below:

0,1,2
0,1,3
0,2,3
0,2,4
Hence the answer 2 3 4.

Series with different number of final steps for second test case are the
following:

0, 10, 20, 30
0, 10, 20, 120
0, 10, 110, 120
0, 10, 110, 210
0, 100, 110, 120
0, 100, 110, 210
0, 100, 200, 210
0, 100, 200, 300

Hence the answer 30 120 210 300.
"""
testCases = int(raw_input())

for _ in range(testCases) :
    steps = int(raw_input()) - 1
    a = int(raw_input())
    b = int(raw_input())
    result = []
    if a < b :
        a, b = b, a
    if a == b :
        print a*steps
        continue
    for counter in range(steps - 1) :
        print counter*a + (steps-counter)*b,

##    for counter in range(steps + 1) :
##        score = counter*a + (steps-counter)*b
##        if score not in result :
##            result.append(score)
##    for score in result :
##        print score,
    print ''

##early fail attempt
##def f7(seq):
##    seen = set()
##    seen_add = seen.add
##    return [ x for x in seq if not (x in seen or seen_add(x))]
##def hashElem():
##    pass
##
##numCases = int(raw_input())
##record = []
##result = []
##for i in range(numCases) :
##    oneRecord = []
##    for _ in range(3) :
##        oneRecord.append(int(raw_input()))
##    record.append(oneRecord)
####print record
##for e in record :
##    a = e[1]
##    b = e[2]
##    oneResult = []
##    tempResult = [0]
##    for tries in range(e[0]-1) :
####        tempResult = run(a,2,2,2)
##        
##        for i in range(len(tempResult)) :
##            tempResult.append(tempResult[i] + b)
##            tempResult[i] = tempResult[i] + a
######        print tempResult
####                        
####        if tempResult not in oneResult :
####            oneResult.append(tempResult)
####        if oneResult not in result :
####            result.append(oneResult)
##"""
##    for num in tempResult :
##        if num not in oneResult :
##            oneResult.append(num)
##    result.append(oneResult)
##     """
####    result = f7(tempResult)
##for oneResult in result :
##    for ele in oneResult :
##        print ele,
##    print ''
