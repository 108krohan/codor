# -*- coding: utf-8 -*-
"""101hack 26 at hackerrank.com
Sherlock and unique substrings

Problem Statement

How often have I said to you that when you have
eliminated the impossible, whatever remains, however improbable,
must be the truth?

Watson gives Sherlock a string S of N characters, say,
S1,S2,...,SN. Now, he defines a substring as a string of
characters Si,Si+1,...Sj where 1≤i≤j≤N. He denotes such
a substring as S[i,j].

Also, he defines a unique substring a substring which occurs only
once in the whole string. For example, in string S =aab,
substrings S[1,2] i.e. aa, S[2,3] i.e. ab, S[3,3] i.e. b and
S[1,3] i.e. aab are unique whereas substrings S[1,1] and S[2,2]
are not unique because both are equal to a.

Now, he gives Sherlock Q queries of form (L,R).
For each such query Sherlock has to report how many
substrings of S[L,R] are one of the unique substrings of S.

:::Input Format:::

The first line contains the string S of N characters,
all of which are lowercase letters. 
The next line contains Q. 
Each of the next Q lines contain a pair of integers denoting
the queries.

:::Output Format:::

For each query, output in one line the required answer.

Constraints

1≤N,Q≤105 
1≤L≤R≤105

Sample Input

aabbab
2
1 3
4 5

Sample Output

2
1

Explanation

Query 1: Two substrings of S[1,3] i.e. aab are unique in the whole
string S. These two substrings are aa and aab.

Query 2: Only one substring of S[4,5] i.e. ba is unique in the
whole string S. This substring is ba.
"""
string = raw_input()
record = []
result = []
numCases = int(raw_input())
for _ in range(numCases) :
    record.append(map(int,raw_input().split()))
for oneCase in record :
    L = oneCase[0]-1
    R = oneCase[1]
    try :
        oneQuery =string[L:L+2]
    except :
        print 1
        continue
    frequency = 0
    for inL in range(L,R) :
        for inR in range(inL+1,R+1) :

            if string[inL:inR] not in string[:inL] and \
               string[inL:inR] not in string[inR:]:
                print string[inL:inR]
                frequency += 1
                continue
    result.append(frequency)
for oneResult in result :
    print oneResult
