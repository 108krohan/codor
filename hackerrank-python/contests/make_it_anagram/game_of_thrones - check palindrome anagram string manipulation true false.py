"""game of thrones at hackerrank.com"""

s = raw_input()
count = {}
for i in range(len(s)):
    if s[i] not in count: count[s[i]] = 0
    count[s[i]] += 1
print count
isPalindrome = True
hasOdd = False
print list(count)
if (sum([count[key] for key in count])): hasOdd = True
##print sum(lambda key : count[key])
for k in count:
    if count[k] % 2 != 0:
        if hasOdd: hasOdd = False
        else:
            isPalindrome = False
            break
print "YES" if isPalindrome else "NO"

"""
https://www.hackerrank.com/contests/magic-lines-september-2015/challenges/game-of-thrones-mglines
"""
