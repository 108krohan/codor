# -*- coding: utf-8 -*-
"""game of thrones at hackerrank.com
"""

"""
Problem Statement

Dothraki are planning an attack to usurp King Robert's throne.
King Robert learns of this conspiracy from Raven and plans
to lock the single door through which the enemy can enter his kingdom.

But, to lock the door he needs a key that is an anagram of
a certain palindrome string.

The king has a string composed of lowercase English letters. Help
him figure out whether any anagram of the string can
be a palindrome or not.

Input Format 

A single line which contains the input string.

Constraints 

1≤ length of string ≤105 
Each character of the string is a lowercase English letter.

Output Format 

A single line which contains YES or NO in uppercase.

Sample Input : 01

aaabbbb

Sample Output : 01

YES

Explanation 

A palindrome permutation of the given string is bbaaabb.
"""
sentence = raw_input()
record = {}
for i in sentence :
    if i not in record :
        record[i] = 1
    else :
        record[i] += 1

odd = 0
for i in record :
    if record[i] % 2 != 0 :
        odd += 1

if len(sentence) % 2 == 0 :
    if odd == 0 :
        print 'YES'
    else :
        print 'NO'
else :
    if odd == 1 :
        print 'YES'
    else :
        print 'NO'
        
