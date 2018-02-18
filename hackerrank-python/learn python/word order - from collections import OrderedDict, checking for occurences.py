# -*- coding: utf-8 -*-
"""Word order at hackerrank.com

Problem Statement

You are given n words. Some words may repeat.
For each word, you have to output its number of occurences.
But the output order should correspond with the order
of the first appearance of the word. See the sample
input/output for clarification. Note that each line in the input
ends with a "\n" character.

Constraints: 
1≤n≤10^5 
Sum of lengths of all the words do not exceed 106 
All words are composed of lowercase-latin alphabets only.

Input Format

First line contains n. 
n lines follow, ith one contains the ith word.

Output Format

Output 2 lines. 
On the first line, output the number of distinct words in the input. 
In the second line, for each distinct word, output its
number of occurences in the order specified in the problem statement.

Sample Input

4
bcdef
abcdefg
bcde
bcdef

Sample Output

3
2 1 1

Explanation

"bcdef" appears twice in the input i.e. in the first and last position, the other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" hence the output.
"""

from collections import OrderedDict
def hashElem(e) :
    result = 0
    for i in e :
        result += ord(i)
    return result%50

numWords = int(raw_input())
##array = set()
uniqueArray = OrderedDict()
uniqueElems = 0

for _ in range(numWords) :
    oneWord = (raw_input())
    if oneWord not in uniqueArray :
        uniqueElems += 1
        uniqueArray[oneWord] = 0
    uniqueArray[oneWord] += 1
print uniqueElems
##print uniqueArray
##for elem in uniqueArray.items :
##    print uniqueArray[elem],
for elem in uniqueArray :
    print uniqueArray[elem],
##    if oneWord not in array :
##        array.add(oneWord)
##        uniqueElems += 1
        
