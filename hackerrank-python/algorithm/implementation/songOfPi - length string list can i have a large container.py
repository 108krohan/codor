# -*- coding: utf-8 -*-
"""song of pi at hackerrank.com
"""
"""
Assume that value of pi is 3.1415926535897932384626433833. You don't
need more
digits for this problem; use the value exactly as it is,
just ignore the floating point and don't perform any
rounding operations.

Input Format

The first line will contain an integer T, representing the
number of test cases. Each of the next
T lines will contain a song. The songs will contain only
English letters (a-z, A-Z) and will contain 1 to 29 words.

Constraints:

No line will contain a total of more than_ 500 _characters.
1≤T≤100
Length of each word is at most 9.

Output Format

For each test case, print "It's a pi song." or
"It's not a pi song." depending on the input.

Sample Input

3
Can I have a large container of coffee right now
Can I have a large container of tea right now
Now I wish I could recollect pi Eureka cried the great
    inventor Christmas Pudding Christmas Pie Is the
    problems very center

Sample Output

It's a pi song.
It's not a pi song.
It's a pi song.
"""
pi = '31415926535897932384626433833'
testCases = int(raw_input())
for _ in range(testCases) :
    result = ''
    stringLst = raw_input().split(' ')
    onePi = pi[:len(stringLst)]
    for word in stringLst :
        result += str(len(word))
    #print result,
    #print onePi
    if result == onePi :
        print "It's a pi song."
    else :
        print "It's not a pi song."
