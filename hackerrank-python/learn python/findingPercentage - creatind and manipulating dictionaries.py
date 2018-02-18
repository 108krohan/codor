"""finding percentage at hackerrank.com
learning how to create and manipulate dictionaries in python.
"""

from __future__ import division
record = {}
numCases = int(raw_input())
for oneCase in range(numCases) :
    details = raw_input().split()
    name = details[0]
    record[name] = "{:.2f}".format((float(details[1]) + float(details[2]) + float(details[3]))/3)
print record[raw_input()]
