# -*- coding: utf-8 -*-
"""alternating characters at hackerrank.com
"""
"""
Shashank likes strings in which consecutive characters
are different. For example, he likes ABABA, while
he doesn't like ABAA. Given a
string containing characters A and B only, he wants to change
it into a string he likes. To do this, he is allowed to delete
the characters in the string.

Your task is to find the minimum number of required deletions.

Input Format

The first line contains an integer T, i.e. the number of test cases. 
The next T lines contain a string each.

Output Format

For each test case, print the minimum number of deletions required.

Constraints

1≤T≤10 
1≤ length of string ≤105

Sample Input

5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Sample Output

3
4
0
0
4
"""


testCases = int(raw_input())

for _ in range(testCases) :
    string = raw_input()
    delete = 0
    for i in range(len(string)-1) :
        if string[i] == string[i+1] :
            delete += 1
    print delete

