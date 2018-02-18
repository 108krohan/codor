"""multiplicative segments at hackerrank.com
"""

def check(size) :
    global result, array, N, K, find_index
    for index in range(N - size - 1) :
        prod = 1
##        print "checking b/w", index, index + size 
        for sub_index in range(index, index + size + 1) :
            prod *= array[sub_index]
        if prod % K == 0 :
##            print size
            result[0].extend([index + 1, index + size + 1])
            find_index = index + 1
            return True
    return False

def find(size) :
    global array, result, N, K, find_index
    result_index = 1
    for index in range(find_index, N - size) :
        prod = 1
##        print "checking b/w", index, index + size
        for sub_index in range(index, index + size + 1) :
            prod *= array[sub_index]
        if prod % K == 0 :
            result[result_index].extend([index + 1, index + size + 1])
            result_index += 1
##    print result 
    return result

K, N = map(int, raw_input().split())
array = [int(i) for i in raw_input().split()]
found = 0
find_index = 0
result = [[] for i in range(N)]
ff_index = 0
for index in range(N) :
    if array[index] % K == 0 :
        found = 1
        result[ff_index] == [index + 1, index + 1]
        ff_index += 1
        print 'found in first'
if found == 0 :
    for size in range(1, N - 1) :
    ##    for subsize in range(i, N - 1) :
        if check(size) :
            found = 1
            break        
if found == 0 :
    print 'NONE'
else :
    print "Minimum interval length:", size + 1
    print "Found intervals:"
    for i in find(size) :
        if i != [] : 
            print i
        else :
            break
"""

Problem Statement


You have an integer K and a list of N integers. Your goal is to find all possible shortest intervals in the list, such that the product of the integers in each interval, is a multiple of K.

Input Format 
 The first line of the input contains two integers K and N.

The second line contains N positive integers,each integer not greater than 1015, separated by a space.

Constraints 
1≤N≤2×105 
1≤K≤1017

Output Format 
 The output should follow the following format:
•If there is no possible interval, it should follow a single line with text “NONE” (without the quotes).
•If at least one interval is found, it should follow a single line saying “Minimum interval length: #” (without the quotes), where # is the length of the shortest possible interval. After that, another line with the phrase “Found intervals:” (without the quotes). Several lines should follow each one denoting a possible shortest interval from the given list in the form [a,b] where a is the starting index and b is the ending index (both inclusive with smallest index being 1). Intervals should be given from the leftmost to the rightmost. 

Sample Input 00
6 5
2 9 4 3 16


Sample Output 00
Minimum interval length: 2
Found intervals:
[1, 2]
[2, 3]
[3, 4]
[4, 5]


Sample Input 01
30 10
15 3 6 4 10 25 21 18 11 5


Sample Output 01
Minimum interval length: 3
Found intervals:
[1, 3]
[3, 5]
[5, 7]
[6, 8]
[8, 10]


Sample Input 02
6 5
7 11 13 17 19


Sample Output 02
NONE


Explanation 
 In first case, we want multiples of 6. Notice that any single integer is by itself, a multiple of 6 so the answers cannot have length 1. The products of the intervals in the output are:
2 * 9 = 18 (6 * 3)
9 * 4 = 36 (6 * 6)
4 * 3 = 12 (6 * 2)
3 * 16 = 48 (6 * 8)



"""
