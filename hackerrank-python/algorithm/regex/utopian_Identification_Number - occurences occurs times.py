"""Utopian Identification Number
"""
import re

validity = re.compile(r'[a-z]{0,3}\d{2,8}[A-Z]{3,}')
testcases = int(raw_input())

for _ in range(testcases) :
    string = raw_input()
    if re.match(validity, string) :
        print 'VALID'
    else :
        print 'INVALID'


"""
Problem Statement

A new identification number is given for every Citizen of the Country Utopia and it has the following format.

The string must begin with between 0-3 (inclusive) lowercase letters.
Immediately following the letters, there must be a sequence of digits (0-9). The length of this segment must be between 2 and 8, both inclusive.
Immediately following the numbers, there must be atleast 3 uppercase letters.
Your task is to find out if a given identification number is valid or not.

Input Format

The first line contains N, N lines follow each line containing an identification number.

Constraints

1 <= N <= 100
Output Format

For every identification number, please print

VALID
if the identification number is valid and print

INVALID
otherwise.

Sample Input

2
abc012333ABCDEEEE
0123AB
Sample Output

VALID
INVALID
Explanation

The first testcase is valid as it starts with 3 letters, followed by 3 integers (max of 8 and min of 2) and ends with more than 3 uppercase letters. 
The second testcase is invalid as it satisfies the first (at least 0 lowercase letters) and the second condition (alteast 2 integers) but fails on the third condition.
"""
