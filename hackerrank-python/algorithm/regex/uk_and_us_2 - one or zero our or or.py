"""uk and us 2 at hackerrank.com
"""

import re

num_lines = int(raw_input())
lines = [raw_input() for i in range(num_lines)]
num_cases = int(raw_input())
for _ in range(num_cases) :

    word_uk = raw_input()
    pattern_string = re.sub('u', "u?", word_uk)
##    print pattern_string
    pattern_string += r"\b"
##    print pattern_string
    num_occurs = 0
    pattern = re.compile(pattern_string)
    for line in lines :
        num_occurs += sum(1 for i in re.finditer(pattern, line))
    print num_occurs

"""
Problem Statement

We've already seen how UK and US words differ in their spelling. One other difference is how UK has kept the usage of letters our in some of its words and US has done away with the letter u and uses just or. Given the UK format of the word that has our in it, find out the total number of occurrences of both its UK and US variants in a given sequence of words.

Input Format

First line contains an integer N. N lines follow, each line contains a sequence of words (W) separated by a single space. 
Next lines contains an integer T. T testcases follow in a new line. Each line contains the UK spelling of a word (W')

Constraints

1 <= N <= 10 
Each line doesn't contain more than 10 words (W) 
Each character of W and W' is a lowercase alphabet. 
If C is the count of the number of characters of W or W', then 
1 <= C <= 20 
1 <= T <= 10 
W' that has our as a sub-string in it.

Output Format

Output T lines and in each line output the number of UK and US version of (W') in all of N lines that contains a sequence of words.

Sample Input

2
the odour coming out of the left over food was intolerable
ammonia has a very pungent odor
1
odour
Sample Output

2
Explanation

In the given 2 lines, we find odour and odor once each. So, the total count is 2.
"""
