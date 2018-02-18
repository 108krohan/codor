# -*- coding: utf-8 -*-
"""pangrams at hackerrank.com
"""
"""
Problem Statement

Pangrams are sentences constructed by using every letter of
the alphabet at least once.

After typing the sentence several times, Roy became
bored with it. So he started to look for other pangrams.

Given a sentence s, tell Roy if it is a pangram or not.

Input Format Input consists of a line containing s.

Constraints 
Length of s can be at most 103 (1≤|s|≤103) and
it may contain spaces, lower case and upper case
letters. Lower case and upper case instances of a
letter are considered the same.

Output Format

Output a line containing pangram if s is
a pangram, otherwise output not pangram.

Sample Input #1

We promptly judged antique ivory buckles for the next prize    
Sample Output #1

pangram
"""
import string
sentence = raw_input().lower()
sentence = ''.join(sentence.split())
data = list(string.ascii_lowercase)
##datalite = map(chr, range(97, 123))
record = ['' for x in range(0,26)]
print record
for elem in sentence :
    if elem not in record :
##        record.insert(ord(elem) - 97, elem)
        print ord(elem) - 97
        record[ord(elem) - 97] = elem
print record
if record == data :
    print "pangram"
else :
    print "not pangram"
    
