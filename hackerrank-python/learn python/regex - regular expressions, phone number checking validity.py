# -*- coding: cp1252 -*-
"""
Problem Statement

Let's dive into the interesting topic of regular expressions!
You are given some inputs and you are required to check whether
they are valid mobile numbers.

A valid mobile number is a ten digit number starting with 7, 8 or 9.

Input Format

The first line contains an integer N followed by N lines,
each containing some string.

Output Format

For every string listed, print YES if it is a valid mobile number
and NO if it isn’t.

Constraints 
1 <= N <= 10 
Mobile Number contains valid alpha-numeric characters 
2 <= len(Number) <= 15

Sample Input

2
9587456281
1252478965

Sample Output

YES
NO
Concept

A valid mobile number is a ten digit number starting with 7, 8 or 9.

Regular expressions are a key concept in any programming
language. A quick explanation with python examples is
available here. You could also go through the link below to
read more about regular expressions in python.

https://developers.google.com/edu/python/regular-expressions
"""
##numCases = int(raw_input())
##result = []
##for _ in range(numCases) :
##    oneNum = raw_input()
##    if len(oneNum) is not 10 :
##        print 'NO'
##    elif oneNum[0] not in ('7', '8', '9') :
##        print 'NO'
##    else :
##        try :
##            oneNum = int(oneNum)
##            print 'YES'
##        except :
##            print 'NO'
##

import re

meta = re.compile(r'(7|8|9)\d{9,9}$')
numCases = int(raw_input())
for _ in range(numCases) :
    num = (raw_input())
    if meta.match(num) :
        print 'YES'
    else :
        print 'NO'
        
