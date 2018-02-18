# -*- coding: utf-8 -*-
"""101hack 26 at hackerrank.com
Sherlock and valid strings.

You know my powers, my dear Watson, and yet at the end
of three months I was forced to confess that I had at
last met an antagonist who was my intellectual equal.

A "valid" string is a string S such that for
all distinct characters in S each such character occurs the
same number of times in S.

For example, aabb is a valid string because the
frequency of both characters a and b is 2,
whereas aabbc is not a valid string because the
frequency of characters a, b, and c is not same.

Watson gives a string S to Sherlock and asks him
to remove some characters from the string such that
the new string is a "valid" string.

Sherlock wants to know from you if it's possible to
be done with less than or equal to one removal.

:::Input Format:::

First and only line contains S, the string Watson gives to Sherlock.

:::Output Format:::

Output YES if string S can be converted to a "valid" string by
removing less than or equal to one character. 
Else, output NO.

Constraints:

1≤size of stringS≤105 
String S contains small alphabets(a-z) only.

Sample Input

aabbcd
Sample Output

NO
Explanation

2 is the minimum number of removals required to
make it a valid string. It can be done in following two ways:

Remove c and d to get aabb. 
Or remove a and b to get abcd.
"""
string = raw_input()
record = []
oneRecord = []
for char in string :
    frequency = 0
    if char in oneRecord :
        continue
    else :
        oneRecord.append(char)
        for oneChar in string :
            if oneChar is char :
                frequency += 1
        record.append(frequency)

##print record
err1 = 0
err2 = 0
cop1 = record[0]
try :
    cop2 = record[1]    
    for ele in record :
        if cop2 is not ele :
            err2 += 1
except :
    pass
for ele in record :
    if cop1 is not ele :
        err1 += 1
if err1 <= 1 or err2 <= 1 :
    print 'YES'
else :
    print 'NO'
    
