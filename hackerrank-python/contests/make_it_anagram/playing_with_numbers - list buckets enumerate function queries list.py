"""playing with numbers at hackerrank.com"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
array = map(int, raw_input().split())
input()
queries = map(int, raw_input().split())
buckets = [0] * 4001
shift = 0
for i in array:
    buckets[i + shift + 2000] += 1 # buckets from -2000 to 2000
count = 0
##print count
for q in queries:
    shift += q
    if shift - q >= 2000 and shift >= 2000:
        s += sum([
    elif shift - q <= -2000 and shift <= -2000:
        s -= 11
    else:
        s = 0
        for i, y in enumerate(buckets):
            val = i + shift - 2000
            s += y * abs(val)
    for i in buckets :
        if i != 0 :
            print i, buckets.index(i), buckets[i]
            count += 1
    print count 
    print s


"""
https://www.hackerrank.com/contests/magic-lines-september-2015/challenges/playing-with-numbers-magic-lines
"""
