# -*- coding: utf-8 -*-
"""Utopian tree at hackerrank.com
Problem Statement

The Utopian Tree goes through 2 cycles of growth every year.
The first growth cycle occurs during the spring, when it doubles in height.
The second growth cycle occurs during the summer, when its height
increases by 1 meter.

Now, a new Utopian Tree sapling is planted at the onset of spring.
Its height is 1 meter.
Can you find the height of the tree after N growth cycles?

:::Input Format:::

The first line contains an integer, T, the number of test cases. 
T lines follow; each line contains an integer, N,
that denotes the number of cycles for that test case.

Constraints 
1≤T≤10 
0≤N≤60

:::Output Format:::

For each test case, print the height of the Utopian Tree after N cycles.
Each line thus has to contain a single integer, only.
"""

results = ()
testcases = ()
T = int(raw_input())
for case in range(T) :
    testcases += (int(raw_input()),)
#print testcases
for case in testcases :
    growth = 1
    for i in range(1,case+1) :
        if i % 2 is not 0 :
            growth *= 2
            #print 'even', growth
        else :
            growth += 1
            #print growth
    print growth    
