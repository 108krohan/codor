# -*- coding: utf-8 -*-
"""funny string at hackerrank.com
"""
"""
Problem Statement

Suppose you have a string S which has length N and
is indexed from 0 to N−1. String R is the reverse
of the string S. The string S is funny if the
condition |Si−Si−1|=|Ri−Ri−1| is true for every i from 1 to N−1.

(Note: Given a string str, stri denotes the ascii value of
the ith character (0-indexed) of str. |x| denotes the
absolute value of an integer x)

Input Format

First line of the input will contain an integer T. T
testcases follow. Each of the next T lines contains one string S.

Constraints

1<=T<=10
2<=length of S<=10000
Output Format

For each string, print Funny or Not Funny in separate lines.

Sample Input

2
acxz
bcxz

Sample Output

Funny
Not Funny

Explanation

Consider the 1st testcase acxz

here

|c-a| = |x-z| = 2
|x-c| = |c-x| = 21
|z-x| = |a-c| = 2
Hence Funny.
"""
testCases = int(raw_input())

for _ in range(testCases) :
    string = raw_input()
    reverse = string[::-1]  #reverse = ''.join(reversed(string)) also works
                            #str[::-1] is an order times faster, however
    result = 'Funny'
    for i in range(1, len(string)) :
        if abs(ord(string[i]) - ord(string[i - 1])) is not \
           abs(ord(reverse[i]) - ord(reverse[i - 1])) :
            result = 'Not Funny'
            break
    if result == 'Not Funny' :
        print result
    else :
        print result
    
    
           
    
