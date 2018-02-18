"""designer door mat at pythonist at hackerrank.com
"""

N, M = map(int, raw_input().split())
design = '.|.'
dashes = '---'

for i in xrange(N/2) :
    print dashes*(N/2 - i) + design*(i + 1) + design*(i) + dashes*(N/2 - i)

center_dashes = M/2 - 3
                                                      
print "-"*center_dashes + 'WELCOME' + "-"*center_dashes
for i in xrange(N/2 - 1, -1, -1) :
    print dashes*(N/2 - i) + design*(i + 1) + design*(i) + dashes*(N/2 - i)
