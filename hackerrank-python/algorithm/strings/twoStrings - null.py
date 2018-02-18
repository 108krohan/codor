"""two strings at hackerrank.com
"""
"""
Problem Statement

You are given two strings, A and B. Find if there
is a substring that appears in both A and B.

Input Format

Several test cases will be given to you in a single
file. The first line of the input will contain a single
integer T, the number of test cases.

Then there will be T descriptions of the test cases. Each
description contains
two lines. The first line contains the string A and
the second line contains the string B.

Output Format

For each test case, display YES (in a newline), if there
is a common substring. Otherwise, display NO.

Constraints

All the strings contain only lowercase Latin letters.
1 <= T <= 10
1 <= |A|, |B| <= 10^5

Sample Input

2
hello
world
hi
world

Sample Output

YES
NO

Explanation

For the 1st test case, the letter o is common between both
strings, hence the answer YES. 
For the 2nd test case, hi and world do not have a common substring,
hence the answer NO.
"""
testCases = int(raw_input())

####a completely different program here. overlook this.
##for _ in range(testCases) :
##
##    record = []
##    for elem in range(testCases) :
##        record.append(raw_input())
##    print record
####    result = list(record[0])

    """the line below finds the shortest string in the list"""
##    result = list(min(record, key = len))  ###this is amazing.
                                
##    print result
##    for char in result[:] :
##        absent = 0
##        for elem in record :
##            if char not in elem :
##                absent = 1
##                break
##        if absent == 1 :
##            result.remove(char)
##    if len(result) >= 1 :
##        print 'YES'
##    else :
##        print 'NO'

for _ in range(testCases) :

    str1 = raw_input()
    str2 = raw_input()
    sets1 = set(str1)
    sets2 = set(str2)
    present = 0
    for elem in sets1 :
        if elem in sets2 :
            present = 1
            break
    if present == 1 :
        print 'YES'
    else :
        print 'NO'
    
    
