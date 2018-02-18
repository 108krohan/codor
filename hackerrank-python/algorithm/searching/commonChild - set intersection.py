"""Common child at hackerrank.com
"""

string_a = raw_input()
string_b = raw_input()

index_a = 0
index_b = 0

list_a = list(string_a)
list_b = list(string_b)
list_a.sort()
list_b.sort()

len_a = len(string_a)
len_b = len(string_b)

shorter = len_a if len_a < len_b else len_a
child = ''

for char in string_a :
    if index_b == len_b :
        break
    while


"""ENTIRELY INCORRECT"""
##string_a = raw_input()
##string_b = raw_input()
##
##set_a = set(string_a)
##set_b = set(string_b)
##
##set_child = set_a.intersection(set_b)
##child = len(set_child)
##
##print child


"""
Problem Statement

Given two strings a and b of equal length, what's the longest string (S) that can be constructed such that it is a child of both? 

A string x is said to be a child of a string y if x can be formed by deleting 0 or more characters from y. 

For example, ‘‘abcd" and ‘‘abdc" has two children with maximum length 3, ‘‘abc" and ‘‘abd". Note that we will not consider ‘‘abcd" as a common child because ′c′ doesn't occur before ′d′ in the second string.

Input format

Two strings, a and b, with a newline separating them.

Constraints

All characters are upper cased and lie between ASCII values 65-90. The maximum length of the strings is 5000.

Output format

Length of string S.

Sample Input #0

HARRY
SALLY
Sample Output #0

2
The longest possible subset of characters that is possible by deleting zero or more characters from HARRY and SALLY is AY, whose length is 2.

Sample Input #1

AA
BB
Sample Output #1

0
AA and BB has no characters in common and hence the output is 0.
"""
