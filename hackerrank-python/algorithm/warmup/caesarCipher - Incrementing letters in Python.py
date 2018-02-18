# -*- coding: utf-8 -*-
#Caesar cipher at Hackerrank.com
"""Julius Caesar protected his confidential information from his enemies
by encrypting it. Caesar rotated every alphabet in the string by
a fixed number K. This made the string unreadable by the enemy.
You are given a string S and the number K.
Encrypt the string and print the encrypted string.

For example: 
If the string is middle-Outz and K=2,
the encoded string is okffng-Qwvb.
Note that only alphabets are encrypted while symbols like - are untouched. 
'm' becomes 'o' when alphabets are rotated twice, 
'i' becomes 'k', 
'-' remains the same because only alphabets are encoded, 
'z' becomes 'b' when rotated twice.

:::Input Format:::

Input consists of an integer N equal to the length of the string,
followed by the string S and an integer K.

Constraints

1≤N≤100 
0≤K≤100 

S is a valid ASCII string and doesn't contain any spaces.

:::Output Format:::

For each test case, print the encoded string.
"""
length = int(raw_input())
string = raw_input()
rotations = int(raw_input())
newString = string
for i in range(rotations):
    newString = ''
    for j in string :
        if j.isalpha() :
            if j is 'z' :
                newString += 'a'
            elif j is 'Z':
                newString += 'A'
            else :
                newString +=  chr(ord(j) + 1)
        else :
            newString += j
    string = newString   
print newString

"""
for i in string:
    if i is not '/' or '*' or '-' or '.' or '(' or ')' or '!' or '\''\
       or '$' or '&' :
        newString += chr(ord(i)+rotations)
"""
