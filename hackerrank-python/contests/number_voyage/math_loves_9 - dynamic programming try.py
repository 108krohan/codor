"""math loves 9 at number voyage at hackerrank.com
"""

##def prof_math(val) :
##    if val == 1 :
##        return 1
##    else :
##        try :
##            return data[val]
##        except :
##            return prof_math(val - 1) + val
##
####val = 999999999999999999999
##val = int(raw_input())
##data = [0, 1]
##for elem in range(2, val) :
##    data.append(prof_math(elem - 1) + elem)
##    print ''
##result1 = prof_math(val)
####res = nums[val]
####print result/val
##for elem in data[1:] :
##    print elem,
import sys
val = 99
##sys.setrecursionlimit(999999999999999999999)
def prof(val) :
    if val == 1 :
        return 1
    else :
        return prof(val - 1) + val
##result = 1
##for i in xrange(2, val) :
##    result = result + i
##print result/val
##print prof(val)
##print prof(val)/val


val = '999999999999999999999'
##val = '999'
result = ''
for elem in val :
    if elem == '9' :
        result += '0'
result = list(result)
result[0] = '5'

print ''.join(result)
"""
Professor Math has a series: 
T(N)={  1 , N = 1
        T(N−1)+N ,N>1
T(N) is the Nth term of the series. Find the value of following: 
T(999999999999999999999)/999999999999999999999
"""
