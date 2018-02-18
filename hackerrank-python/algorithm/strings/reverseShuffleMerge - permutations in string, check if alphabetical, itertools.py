# -*- coding: utf-8 -*-
"""reverse shuffle merge at hackerrank.com
"""
"""
you can also use itertools.permutations

=======================================================================
To get all the permutations of a given string :

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
-------------------------------------------------------------------
Skimmed down version :
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
--------------------------------------------------------------------

The algorithm is:

Remove the first letter
Find all the permutations of the remaining letters (recursive step)
Reinsert the letter that was removed in every possible location.
The base case for the recursion is a single letter. There is only one
way to shuffle a single letter.

Worked example

Imagine the start word is bar.

First remove the b.
Find the permuatations of ar. This gives ar and ra.
For each of those words, put the b in every location:
ar -> bar, abr, arb
ra -> bra, rba, rab

from itertools import permutations
>>> perms = [''.join(p) for p in permutations('stack')]
>>> perms
======================================================================
check if a string is alphabetical or not :

def isInAlphabeticalOrder(word) :
    return word == ''.join(sorted(word))

def isInAlphabeticalOrder(word):
    return all((word[i+1] >= word[i] for i in range(len(word) - 1)))

def isInAlphabeticalOrder(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True

all(x <= y for x, y in zip(word, word[1:]))
======================================================================
"""

def reverse(S) :
    return S[::-1]

def shuffle(word):
    stack = list(word)
    results = [stack.pop()]
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results

def merge(reverse, word) :
    result = []
    end = len(reverse)
    for start in range(len(reverse)) :
        for i in range(len(word)) :
            oneResult = reverse[:start] + word[:i] + \
                        reverse[start:end] + word[i:]
            if oneResult == data :
                return True
    return False

import string
data = raw_input()
elems = []

for letter in data :
    occurs = data.count(letter)
    if letter not in elems :
        for oneOccur in range(occurs/2) :
            elems.append(letter)

possibleA = shuffle(''.join(elems))
possibleA.sort()
smallestA = possibleA[0]

for word in possibleA :

    if merge(word[::-1],word, data) :
        if all(x <= y for x, y in zip(word, word[1:])) :
            smallestA = word
            break
        if smallestA > word :
            smallestA = word
            break
print smallestA

"""
def reverse(S) :

    return S[::-1]

def shuffle(string):
    if len(string) == 0:
        return ['']
    prevList = shuffle(string[1:len(string)])
    nextList = []
    for i in range(0,len(prevList)):
        for j in range(0,len(string)):
            newString = prevList[i][0:j]+string[0]+prevList[i][j:len(string)-1]
            if newString not in nextList:
                nextList.append(newString)
    return nextList

def merge(reverse, word) :

##    strs1 = S1
##    s2 = S2
##    numElems = 2*len(strs1)*len(s2)
##    result = ['' for i in range(numElems)]
##    print result
##    print 'reverse =', reverse
##    print 'word =', word
    result = []
    end = len(reverse)
    for start in range(len(reverse)) :
##        for end in range(len(reverse)) :
##            if start <= end :
            for i in range(len(word)) :
                oneResult = reverse[:start] + word[:i] + \
                            reverse[start:end] + word[i:]
##                print 'oneResult =', oneResult,
##                print '||  start =', start,
##                print ' |  and end =', end,
##                print ' |  at i =', i,
##                print ' ||'
##                    if oneResult not in result :
##                        print 'oneResult =', oneResult,
##                        print '||  start =', start,
##                        print ' |  and end =', end,
##                        print ' |  at i =', i,
##                        print ' ||'
                result.append(oneResult) 

##    for i in range(0, numElems, 2) :
##        for char1, char2 in zip(strs1,s2) :
##            result[i] += char1
##            result[i+1] += char2

##    print result
    return result

import string
data = raw_input()
##print data
elems = []

for letter in data :
    occurs = data.count(letter)
    if letter not in elems :
        for oneOccur in range(occurs/2) :
            elems.append(letter)

##print elems
possibleA = shuffle(''.join(elems))
##print possibleA
possibleA.sort()
##print possibleA
smallestA = possibleA[0]

for word in possibleA :

    if data in merge(word[::-1],word) :
##        print data
##        print smallestA > word
##        print all(x <= y for x, y in zip(word, word[1:]))
        if all(x <= y for x, y in zip(word, word[1:])) :
            smallestA = word
            break
        if smallestA > word :
            smallestA = word
            break
print smallestA
"""
"""
Problem Statement

Given a string, S, we define some operations on the string as follows:

a. reverse(S) denotes the string obtained by reversing string S. E.g.: reverse("abc") = "cba"

b. shuffle(S) denotes any string that's a permutation of string S. E.g.: shuffle("god") ∈ ['god', 'gdo', 'ogd', 'odg', 'dgo', 'dog']

c. merge(S1,S2) denotes any string that's obtained by interspersing the two strings S1 & S2, maintaining the order of characters in both. 
E.g.: S1 = "abc" & S2 = "def", one possible result of merge(S1,S2) could be "abcdef", another could be "abdecf", another could be "adbecf" and so on.

Given a string S such that S∈ merge(reverse(A), shuffle(A)), for some string A, can you find the lexicographically smallest A?

Input Format

A single line containing the string S.

Constraints: 
S contains only lower-case English letters.
The length of string S is less than or equal to 10000.

Output Format

A string which is the lexicographically smallest valid A.

Sample Input

eggegg
Sample Output

egg
Explanation

reverse("egg") = "gge" 
shuffle("egg") can be "egg" 
"eggegg" belongs to merge of ("gge", "egg")

The split is: e(gge)gg.

egg is the lexicographically smallest.
"""
