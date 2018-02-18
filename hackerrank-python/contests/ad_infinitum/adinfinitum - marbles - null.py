# -*- coding: utf-8 -*-
"""infinitum12 marbles at hackerrank.com
"""
"""
Problem Statement

Nam has N marbles, currently put in a straight line on
a table. Marbles are numbered from 1 through N from left to
right. For each i (1≤i<N), marble
number i and marble number i+1 are adjacent to each other.

Now, Nam is taking all N marbles to his bag. He will do it arcording to following rules:

Nam can start from any marble.
Except the first marble taken, the marble taken must be adjacent to one of previous marbles taken before.
Your task is count the number of ways of taking N marbles. Two way are consider different if ordering of taking marbles are different. Since the answer maybe large, you must print it modulo 1000000007 or (109+7).

Input Format 
The first line contains the number of test cases T. Then T test cases follow.

Each test is described in a single line contains a single integer N - the number of marbles.

Output Format 
For each test, print the number of ways taking marbles modulo 1000000007.

Constraints 
1≤T≤100 
1≤N≤109
Sample Input

2
1
3
Sample Output

1
4
Explaination

In the second case (N=3), there are 4 ways of taking marbles. They are:

Taking marble number 1 first; then marble 2, 3.
Taking marble number 2 first; then 1, 3.
Taking marble number 2 first; then 3, 1.
Taking marble number 3 first; then marble 2, 1.
"""
import math
testCases = int(raw_input())
for _ in range(testCases) :
    numWays = 0
    numMarbles = int(raw_input())
    marbles = [x for x in range(1,numMarbles + 1)]
##    for oneMarble in marbles[:] :
##        newMar = marbles[:]
##        newMar.remove(oneMarble)
##        while newMar :
##    for i in range(1, numMarbles+1) :
##        numWays += 2**abs(int(math.ceil(numMarbles/2)) - i)
    numWays = 2*1*(2**(numMarbles/2)-1)
    if numMarbles % 2 != 0 :
        numWays += 2**(numMarbles/2)
    if numMarbles == 1 :
        print 1
        continue
    else :
##        print (2 + (2**(numMarbles-1))*(numMarbles-2))%(10**9 + 7)
        print numWays%(10**9 + 7)        
        
