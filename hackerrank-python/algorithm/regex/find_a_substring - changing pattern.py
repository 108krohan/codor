"""find substring at hackerrank.com
"""
"""
sum(1 for m in re.finditer(thepattern, thestring)) (to avoid ever materializing
the list when all you care about is the count) are also quite possible.
Somewhat idiosyncratic would be using subn and ignoring the
resulting string...:

def countnonoverlappingrematches(pattern, thestring):
  return re.subn(pattern, '', thestring)[1]
the only real advantage of this latter idea would come if you
only cared to count (say) up to 100 matches; then, re.subn(pattern, '',
thestring, 100)[1] might be practical (returning 100 whether there are
100 matches, or 1000, or even larger numbers).

Counting overlapping matches requires you to write more code.
Assuming for example that you want possibly-overlapping matches
starting at distinct spots in the string

def countoverlappingdistinct(pattern, thestring):
  total = 0
  start = 0
  there = re.compile(pattern)
  while True:
    mo = there.search(thestring, start)
    if mo is None: return total
    total += 1
    start = 1 + mo.start()

Note that you do have to compile the pattern into a RE object in this
case: function re.search does not accept a start argument (starting
position for the search) the way method search does, so you'd have to
be slicing thestring as you go -- definitely more effort than just having
the next search start at the next possible distinct starting point, which is
what I'm doing in this function.
"""

"""
[m.start() for m in re.finditer('(?=tt)', 'ttt')]

overlaps :
 s = 'tt'
 [m.start() for m in re.finditer('(?=%s)(?!.{1,%d}%s)' % (search, \
 len(search)-1, search), 'ttt')]
"""

import re
num_strings = int(raw_input())
strings = [raw_input() for i in xrange(num_strings)]
num_words =int(raw_input())
for i in range(num_words) :
    word = raw_input()
    pattern = re.compile(r'(?<=([a-z]|[A-Z]|[_]|\n))' + \
                         word + r'(?=([a-z]|[A-Z]|[_]|\n))')
    num_occurs = 0
    for the_string in strings :
        num_occurs += sum(1 for m in re.finditer(pattern, the_string))        
    print num_occurs


"""

Problem Statement

A word made of a series of letters ( lower or upper ) or numerics
or an underscore _ ( ascii value 95).

We define a substring as follows.

It is a part of a word.
The given substring must be preceeded and succeeded by letters or
numerics or an underscore.
A word will be surrounded by 1 or more occurrences of non-letter,
non-numeric and non-underscore ( not an underscore )
characters - or the beginning or end of a line on one side.

<non letter, non-numeral ,non-underscore ><letters, numerals and
underscore><non letter, non numerals, non underscore>

Given a sentence, can you find the total number of occurrences of
the substring?

Input Format

First line is an integer N, N lines follow. Each line is a sentence
as per the above definition. 
Nth sentence is immediately followed by an integer T, T lines follow. 
Each line has a lists a substring on which you need to perform the
prescribed query which return the total number of occurrences of the
substring.

Constraints

1 <= N <= 100 
1 <= T <= 10

Output format

For every word, print the total number of occurrences of the substring
in all of the N sentences provided as input.

Sample Input

1
existing pessimist optimist this is
1
is
Sample Output

3
Explanation

'existing' has 'is' as a substring and is both preceded and succeeded
by words as defined above.
'pessimist' has 'is' as a substring for the same argument as
above.
'optimist' has 'is' as a substring for the same
argument as above.
'this' though has 'is' as a substring is only preceded by a word
and is succeeded by a [blank space] which is non-letter, non-numeric and
non-underscore
'is' is not included as it is preceded and succeeded by a [blank space]
which is non-letter, non-numeric and non-underscore.
"""
