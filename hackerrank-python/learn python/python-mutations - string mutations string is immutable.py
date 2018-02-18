"""python mutations at hackerrank.com

What if you would like to assign a value?

>>> string[5] = 'k' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment


How would you approach this?

One solution is to convert the string to a list and then change the value.
Example

>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra

Another approach is to slice the string and join it back.
Example

>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra


Task 
You have to read a string. change the character
at a given index and print the string.

Input Format 
First line contains a string, S. 
Next line contains an integer i and a character c.

Output Format 
Using any of the method explained above.
Replace the character at index i with c.

Sample Input

abracadabra
5 k
"""
##string = raw_input()
##a = raw_input().split()
##a[0] = int(a[0])
##string = string[:a[0]] + str(a[1]) + string[a[0]+1:]
##print string

string = input().split()
string.capitalize()
sub = input().split()
sub.capitalize()
count = 0
while sub in string :
    count +=1
    string = string[(string.index(sub)):]
