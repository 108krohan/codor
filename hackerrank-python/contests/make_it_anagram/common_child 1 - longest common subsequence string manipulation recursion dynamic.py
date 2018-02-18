"""common child 1 at hackerrank.com
"""

from __future__ import division
from sys import stdin
from collections import defaultdict

def lcs(s1, s2):
    prev = defaultdict(int)
    for i in range(len(s1)):
        cur = defaultdict(int)
        for j in range(len(s2)):
            cur[j] = 1 + prev[j-1] if s1[i] == s2[j] else max(cur[j - 1], prev[j])
        prev = cur
    print cur
    print prev
    print ''
    return prev[len(s2)-1]
                
def main():
    s, t = stdin.next().strip(), stdin.next().strip()
    print lcs(s, t)

main()

"""
https://www.hackerrank.com/contests/magic-lines-september-2015/challenges/common-child-magic-lines
"""
