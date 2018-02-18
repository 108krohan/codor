# -*- coding: utf-8 -*-
"""bigger is greater at hackerrank.com
"""
def bigger_is_greater(word, index, point_of_difference) :
    not_found = True
    for rev_index in range(index - 1, point_of_difference - 1, -1) :
        for rev_subindex in range(rev_index - 1, point_of_difference, -1) :
            if word[rev_index] > word[rev_subindex] :
                not_found = False
                return bigger_is_greater(word, rev_index, rev_subindex)
    if not_found :
        return index, point_of_difference
    
testcases = int(raw_input())

for _ in range(testcases) :
    greater = False
    word = raw_input()
    bigger_word = ""
    num_letters = len(word)
    point_of_difference = 0
    sub = 0
    for index in range(num_letters - 1, 0, -1) :
        for subindex in range(index - 1, -1, -1) :
            if word[index] > word[subindex] :
                greater = True
##                print "\nFrom behind : \t index =", num_letters - index,
##                print "letter :", word[index],
##                print "\n \t\t subindex =" , num_letters - subindex,
##                print "letter :", word[subindex]
                sub, point_of_difference = bigger_is_greater(word, index, subindex)
##                print point_of_difference                                        
##                print bigger_word,
                break
##        print ''
        if greater :
            break
    if not greater :
        print 'no answer'
##        print ''
    else :
        new_word = word[:point_of_difference] + word[sub] + \
                   word[point_of_difference + 1:sub] + \
                   word[point_of_difference] + word[sub + 1:]
        rest_of_letters = [new_word[i] for i in range(num_letters) \
                           if i > point_of_difference ]
        rest_of_letters.sort()
##        print "\t\trest_of_letters =", rest_of_letters
        resulting_word = new_word[:point_of_difference + 1] + \
                         "".join(rest_of_letters)
##        print "\t\t", word
##        print "\t\t", resulting_word
        print resulting_word                           
##        bigger_word = bigger_is_greater(bigger_word, word, point_of_difference)

##import itertools
##testCases = int(raw_input())
##
##for _ in range(testCases) :
##
##    word = raw_input()
##
##    noAnswer = True
##    set_words = list(set(map("".join, itertools.permutations(word))))
##    set_words.sort()
####    print set_words
##    try :
##        print set_words[set_words.index(word) + 1]
##    except :
##        print 'no answer'
     
##def bigger_is_greater(bigger_word, word, index = 0 ) :
##    
##    if index == len(bigger_word) - 1 :
##        return bigger_word
##
##    while bigger_word[index] != word[index] :
##            index += 1
##    smallest_rest_letter = min(bigger_word[index:])
##    if bigger_word[index] == smallest_rest_letter :
##        return bigger_word
##
##    else :
##        
##        bigger_word =
##    
##    print bigger_word
        
"""
Problem Statement

Given a word w, rearrange the letters of w to construct another word s in such a way that s is lexicographically greater than w. In case of multiple possible answers, find the lexicographically smallest one.

Input Format

The first line of input contains t, the number of test cases. Each of the next t lines contains w.

Constraints 
1≤t≤105 
1≤|w|≤100 
w will contain only lower-case English letters and its length will not exceed 100.

Output Format

For each testcase, output a string lexicographically bigger than w in a separate line. In case of multiple possible answers, print the lexicographically smallest one, and if no answer exists, print no answer.

Sample Input

5
ab
bb
hefg
dhck
dkhc
Sample Output

ba
no answer
hegf
dhkc
hcdk
Explanation

Test case 1: 
There exists only one string greater than ab which can be built by rearranging ab. That is ba.
Test case 2: 
Not possible to rearrange bb and get a lexicographically greater string.
Test case 3: 
hegf is the next string lexicographically greater than hefg.
Test case 4: 
dhkc is the next string lexicographically greater than dhck.
Test case 5: 
hcdk is the next string lexicographically greater than dkhc.
"""
"""
input :
2
bpgqfwoyntuhkvwo
schtabphairewhfmp

output :
bpgqfwoyntuhkwov
schtabphairewhfpm
"""

