"""largest permutations at hackerrank.com
"""

import sys


line = sys.stdin.readline()
tokens = line.split(" ")
N = int(tokens[0])
K = int(tokens[1])

line = sys.stdin.readline()
tokens = line.split(" ")


original = [int(elem) for elem in tokens]


sorted = list(original)

sorted.sort(reverse =True)

def permute(list,i1,i2):
      tmp = list[i1]
      list[i1] = list[i2]
      list[i2] = tmp


current = 0
while (K > 0 and current< (len(sorted)-1)):
   if(original[current] <> sorted[current]):
      permute(???)
      K-=1
   current+=1
      

print ' '.join(map(str,original))
"""
https://www.hackerrank.com/contests/magic-lines-september-2015/challenges/largest-permutation-magic-lines
"""
"""
Output Format 
Print the lexicographically largest permutation you can make with at most K swaps.

Constraints 
1≤N≤105 
1≤K≤109

Sample Input#00

5 1
4 2 3 5 1
Sample Output#00

5 2 3 4 1
Explanation#00 
You can swap any two numbers in [4,2,3,5,1] and see the largest permutation is [5,2,3,4,1]
Sample Input#01

3 1
2 1 3
Sample Output#01

3 1 2
Explanation#01 
With 1 swap we can get [1,2,3], [3,1,2] and [2,3,1] out of these [3,1,2] is the largest permutation.

Sample Input#02

2 1
2 1
Sample Output#02

2 1
Explanation#02 
We can see that [2,1] is already the largest permutation. So we don't need any swaps.
"""
