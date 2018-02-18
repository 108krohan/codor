"""python tuples at hackerrank.com
hash is a built in function in __builtin__ module
"""


N = int(raw_input())
record = map(int, raw_input().split())
T = ()
for i in range ( N ) :
    T += (record[i],)
hash(T)
print hash(T)
