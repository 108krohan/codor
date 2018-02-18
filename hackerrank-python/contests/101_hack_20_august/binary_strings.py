"""binary strings at 101 hack hackerrank.com
"""

"""expect code misalignment"""
def solve(s,n,k,t):
     if k >= n or t == 0:
         return s
     l = []
     for i in xrange(k):
         l.append([])
     for i in xrange(n):
         if s[i] == '1':
             l[i%k].append(i)
             r = 0
             ss = ''
     for i in xrange(n):
         if len(l[i%k]) > 0:
             d = (l[i%k][0]-i)/k
         if r + d <= t:
             ss += '1'
             r += d
             del l[i%k][0]
     else:
         ss += '0'
     else:
         ss += '0'
 
 n,k,t = map(int,raw_input().split())
 s = raw_input()
 print solve(s,n,k,t)
