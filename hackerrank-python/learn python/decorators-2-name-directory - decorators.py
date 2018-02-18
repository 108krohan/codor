"""decorators 2 name directory at hackerrank.com
"""
"""
"""
N = int(raw_input())
dis = {'M':'Mr.', 'F':'Ms.'}
record = []
for _ in range(N) :
    first, last, age, sex = raw_input().split()
    record.append([dis[sex],first, last, int(age), sex])
record.sort(key = lambda oneRecord : oneRecord[3])
for ele in record :
    print ele[0], ele[1], ele[2]
    
