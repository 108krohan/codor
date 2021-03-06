# -*- coding: utf-8 -*-
"""
Problem Statement

DefaultDict is a container in the collections class of Python. It is almost the same as the usual dictionary (dict) container but with one difference. The value fields' data-type is specified upon initialization. 
A basic snippet showing the usage follows:

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i

This prints:

('python', ['awesome', 'language'])
('something-else', ['not relevant'])

In this challenge, you will be given 2 integers
(n and m) and n words which might repeat, say they
belong to a word group A. Then you'll be given m
other words belonging to word group B. For each
of these m words, you have to check whether the word
has appeared in A or not. If it has then
you have to print indices of all of its occurences. If it
has not then just print −1.

Constraints 
1≤n≤10000 
1≤m≤100 
1≤ length of each word in the input≤100
Input Format

The first line contains n and m. 
The next n lines contain the words belonging to A. 
The next m lines contain the words belonging to B.

Output Format

Output m lines. 
The ith line should contain the 1 indexed positions of
occurences of the ith word, separated by spaces, of
the last m lines of the input.

Sample Input

5 2
a
a
b
a
b
a
b

Sample Output

1 2 4
3 5

Explanation

'a' appeared 3 times in positions 1, 2 and 4.
'b' appeared 2 times in position 3 and 5. Hence the output. For
the same word group A, had the appearances of 'c'
been asked about in the word group B, you would have had
to print −1 instead.


from collections import defaultdict

"""
from collections import defaultdict
N,M = map(int, raw_input().split())
result = defaultdict(list)
record = []
checker = []

for i in range(N) :
    record.append(raw_input())

for i in range(M) :
    checker.append(raw_input())
    if checker[i] in record :
        for j in range(N) :
            if record[j] == checker[i] :
                result[i].append(j)
    else :
        result[i].append(-2)
for i in range(M):
    for j in result[i] :
        print j+1,
    print ''
