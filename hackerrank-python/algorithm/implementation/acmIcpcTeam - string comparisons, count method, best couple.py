# -*- coding: utf-8 -*-
"""acm icpc team at hackerrank.com
"""
"""
Problem Statement

You are given a list of N people who are attending
ACM-ICPC World Finals. Each of them are either well versed in
a topic or they are not. Find out the maximum number of topics
a 2-person team can know. And also find out how many teams can
know that maximum number of topics.

Note Suppose a, b, and c are three different people, then (a,b)
and (b,c) are counted as two different teams.

Input Format

The first line contains two integers, N and M, separated by
a single space, where N represents the number of people, and M
represents the number of topics. N lines follow.
Each line contains a binary string of length M. If the ith line's
jth character is 1, then the ith person knows the jth topic; otherwise,
he doesn't know the topic.

Constraints 

2≤N≤500 
1≤M≤500

Output Format

On the first line, print the maximum number of topics a
2-person team can know. 
On the second line, print the number of 2-person teams that can
know the maximum number of topics.

Sample Input

4 5
10101
11100
11010
00101

Sample Output

5
2

Explanation

(1, 3) and (3, 4) know all the 5 topics. So the maximal topics
a 2-person team knows is 5, and only 2 teams can achieve this.
"""

import string
##testCases = int(raw_input())
numPeople, numTopics = map(int, raw_input().split())
record = []
for _ in range(numPeople) :
    record.append(raw_input())
best = 0
couple = 0
for oneP in range(numPeople) :

    for twoP in range(oneP + 1, numPeople) :

        onePTopics = record[oneP]
        twoPTopics = record[twoP]

        count = numTopics
        for i in range(numTopics) :
            if onePTopics[i] == '0' and twoPTopics[i] == '0' :
                count -= 1
##        print count,
##        print couple, best
        if count > best :
            best = count
            couple = 1
        elif count == best :
            couple += 1
        else :
            pass
print best
print couple
