"""counting sort 1 at hackerrank.com
"""
"""
General Summary : Count the number of times a number from 0 to 99 occur in
an array containing numbers from the range
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def counting_sort() : 
    global array 
    result = [0 for i in range(100)]
    for elem in array : 
        result[elem] += 1
    print " ".join(str(i) for i in result)

size = int(raw_input())
array = [int(i) for i in raw_input().strip().split()]
counting_sort()

