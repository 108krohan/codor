"""xml-1-find-the-score at hackerrank.com
"""
"""
Problem Statement

You are given a valid XML document and you have to print
its score. The first line of input is the number of XML
lines followed by the XML lines. Score is given by the sum
of score of each element. For any element, score is equal to the
number of attributes it has.

Input Format

The first line shows the number of lines in XML document followed
by the XML document.

Output Format

An integer score

Sample Input

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Sample Output

5

Explanation

The feed and subtitle tag have one attribute each lang,
title and updated tags have no attribute and link tag has
three attributes rel, type and href So the total score is 1 + 1 + 3 = 5 

There maybe any level of nesting in the XML document. To learn
about XML parsing, refer here. 
NOTE : In order to parse and generate XML element tree, use the
following code

import xml.etree.ElementTree as etree
tree = etree.ElementTree(etree.fromstring(xml))

Here xml is the variable containing the string.
Also, to find the number of keys in a dictionary, use the len function.

dicti = {'0': 'This is zero', '1': 'This is one'}
print (len(dicti))
"""

"""
lines = int(input())

##this one uses recursion

def count_of_attr(root):
    count = len(root.attrib)
    for child in root:
        count += count_of_attr(child)
    return count

import xml.etree.ElementTree as etree
count = 0
xml = ''
for i in range(lines):
    xml += input()

tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()
count = count_of_attr(root)
    
print(count)
"""

n = int(raw_input())
xml = ""
for i in range(n):
    xml += raw_input()
import xml.etree.ElementTree as etree
tree = etree.ElementTree(etree.fromstring(xml))
score = 0
for elem in tree.iter():
	score += len(elem.attrib)
print score


####root = tree.getroot()
####for child in root :
####    print child
"""getaway"""
"""
count = 0
lines = int(raw_input())
for i in range(lines) :
    string = raw_input()
    chief = string.index('<')
    for j in range(chief, string.index('>')) :
        if string[j] == ' ' :
            count += 1
print count
"""
