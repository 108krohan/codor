"""uk and us at hackerrank.com
"""
import re

def counter(us, uk) :
    global sentences
    one_count = 0 
    for sent in sentences :
##        print re.findall(us,sent),
##        print re.findall(uk,sent)
        one_count += len(re.findall(us, sent)) + len(re.findall(uk, sent))
    return one_count
sents = int(raw_input())
sentences = ()
for _ in range(sents) :
    sentences += (raw_input(),)
testcases = int(raw_input())
for _ in range(testcases) :
    us = raw_input()
    uk = re.sub(r'z','s',us)
    count = counter(us, uk)
    print count

"""
Make a dict-typed frequency table for your words, then iterate over the words in your string.

vocab = ["foo", "bar", "baz"]
s = "foo bar baz bar quux foo bla bla"

wordcount = dict((x,0) for x in vocab)
for w in re.findall(r"\w+", s):
    if w in wordcount:
        wordcount[w] += 1
Edit: if the "words" in your list contain whitespace, you can instead build an RE out of them:

from collections import Counter

vocab = ["foo bar", "baz"]
r = re.compile("|".join(r"\b%s\b" % w for w in vocab))
wordcount = Counter(re.findall(r, s))
Explanation: this builds the RE r'\bfoo bar\b|\bbaz\b' from the vocabulary. findall then finds the list ['baz', 'foo bar'] and the Counter (Python 2.7+) counts the occurrence of each distinct element in it. Watch out that your list of words should not contain characters that are special to REs, such as ()[]\.
"""
"""
Problem Statement

American English and British English differ in several aspects which
are reflected in their spelling. One difference frequently observed,
is that words written in American English, which have a suffix ze often
end in se in British English. Given the American-English spelling
of a word which ends in ze your task is to find the total count of
all its British and American variants in all the given sequences of
words. i.e. you need to account for the cases where the word occurs as
it is given to you (i.e. the version ending in -ze) and you also
need to find the occurances of its British-English counterparts
(i.e, the version ending in -se).

Input Format

First line contains N, N lines follow each line contains a sequence
of words (W) separated by a single space. Next line contains T.
T testcases follow in a new line. Each line contains the American
English spelling of a word (W')

Constraints

1 <= N <= 10 
Each line doesn't contain more than 10 words (W) 
Each character of W and W' is a lowercase alphabet. 
If C is the count of the number of characters of W or W', then 
1 <= C <= 20 
1 <= T <= 10 
W' ends with ze ( US version of the word)

Output Format

Output T lines and in each line output the total number of
American and British versions of (W') in all of N lines that
contains a sequence of words.

Sample Input

2
hackerrank has such a good ui that it takes no time to familiarise its environment
to familiarize oneself with ui of hackerrank is easy
1
familiarize

Sample Output

2

Explanation

In the given 2 lines, we find familiarize and familiarise once
each. So, the total count is 2.
"""
