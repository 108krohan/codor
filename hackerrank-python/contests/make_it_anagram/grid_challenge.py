"""grid challenge at hackerrank.com
"""
for _ in xrange(input()):
    A = []
    ans = "YES"
    n = input()
    for i in xrange(n):
        A.append(raw_input().strip())
    for i in xrange(n - 1):
        x, y = ???
        for j in xrange(n):
            if x[j] > y[j]:
                ans = "NO"
    print ans

"""
https://www.hackerrank.com/contests/magic-lines-september-2015/challenges/grid-challenge-magic-lines
"""
    
"""
Sample Input

1
5
ebacd
fghij
olmkn
trpqs
xywuv
Sample Output

YES
Explanation

The grid in the first and only testcase can be reordered to

abcde
fghij
klmno
pqrst
uvwxy
"""
