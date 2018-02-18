# -*- coding: utf-8 -*-
"""anagram at hackerrank.com
"""
"""
from itertools import permutations
>>> perms = [''.join(p) for p in permutations('stack')]
>>> perms
"""
##from itertools import permutations
##
##def anagramic_pairs(word, length, anagram_pairs = 0) :
##
##    for bunch in range(1, length) :
##        for index in range(length - bunch) :
####            for sub_index in range(bunch, length) :
##            substring = word[index:index + bunch]
##            print substring,
####            anagrams = get_anagrams(substring)
####            for unagram in anagrams :
##            for unagram in (permutations(substring)) :
##                unagram = ''.join(unagram)
####                print unagram 
##                if unagram in word[index + 1:] :
##                    anagram_pairs += 1
##                    break
##            print ''
##    return anagram_pairs
##

from itertools import permutations

"""
####this function is heavy, for two remove operations with O(n) complexity

def check_anagram(word_one, word_two, bunch) :
    word_list_one = list(word_one)
    word_list_two = list(word_two)
    index = 0
    while word_list_one != [] and word_list_two != [] :
        letter = word_list_one[index]
##        print letter
        if word_list_one[index] in word_list_two :
            word_list_two.remove(letter)
            word_list_one.remove(letter)
        else :
            return False
    if word_list_one == [] and word_list_two == [] :
        return True
    return False
"""

def check_anagram(word_one, word_two, bunch) :
    index = 0
    word_two = list(word_two)
    while index < bunch :
        if word_one[index] not in word_two :
            return False
        word_two.remove(word_one[index])
        index += 1
    return True

def anagramic_pairs(word, length, anagram_pairs = 0) :

    for bunch in range(1, length) :
        for index in range(length - bunch) :
            substring_one = word[index:index + bunch]
            for subindex in range(index + 1, length - bunch + 1) :
                substring_two = word[subindex:subindex + bunch]
                
                if check_anagram(substring_one, substring_two, bunch) :
##                    print substring_one, substring_two
##                    print index, subindex, bunch,
##                    print 'tick'
                    anagram_pairs += 1
##                    anagram_pairs 
##                    break
##                print ''
    return anagram_pairs


testcases = int(raw_input())

for _ in range(testcases) :

    word = raw_input()
    length = len(word)
    pairs = anagramic_pairs(word, length)
    print pairs

    


"""
def permute3(s):
    return [s] if len(s) == 1 else [ \
    c + perm for i, c in enumerate(s) for perm in permute3( \
    s[:i]+s[i+1:])]
"""


"""
Problem Statement

Sid is obsessed with reading short stories. Being a CS
student, he is doing
some interesting frequency analysis with the
books. He chooses strings S1 and S2
in such a way that |len(S1)−len(S2)|≤1.

Your task is to help him find
the minimum number of characters of the first
string he needs to change to enable him to
make it an anagram of the second string.

Note: A word x is an anagram of another
word y if we can produce y by rearranging the letters of x.

Input Format

The first line will contain an integer,
T, representing the number of test cases. Each test
case will contain a string having length
len(S1)+len(S2), which will be concatenation of both
the strings described above in the problem.The given
string will
contain only characters from a to z.

Output Format

An integer corresponding to each test case is printed
in a different line, i.e. the number of changes
required for each test case. Print −1 if it is not possible.

Constraints

1≤T≤100
1≤len(S1)+len(S2)≤104

Sample Input

6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx

Sample Output

3
1
-1
2
0
1
Explanation 
Test Case #01: We have to replace all least three characters
from the first string to make both of strings
anagram. Here, S1 = "aaa" and S2 = "bbb". So the
solution is to replace all character 'a' in string a with
character 'b'. 
Test Case #02: You have to replace 'a' with 'b', which
will generate "bb". 
Test Case #03: It is not possible for two strings of
unequal length to be anagram for each other. 
Test Case #04: We have to replace both the characters of
first string ("mn") to make it anagram
of other one. 
Test Case #05: S1 and S2 are already anagram to each
other. 
Test Case #06: Here S1 = "xaxb" and S2 = "bbxx". He
had to replace 'a' from S1 with 'b' so that S1 = "xbxb" and
we can rearrange its letter to "bbxx" in order to get S2.
"""

##testCases = int(raw_input())
##for _ in range(testCases) :
##    
##    s1s2 = raw_input()
##    if len(s1s2) % 2 != 0 :
##        print -1
##        continue
##    
##    middle = len(s1s2) / 2
##    s1 = list(s1s2[:middle])
##    s2 = list(s1s2[middle:])
##    for letter in s1[:] :
##        if letter in s2 :
##            s1.remove(letter)
##            s2.remove(letter)
####            print s1, s2
##    print len(s1)

"""
input :
5
ifailuhkqq
hucpoltgty
ovarjsnrbf
pvmupwjjjf
iwwhrlkpek

output :
3
2
2
6
3
"""
