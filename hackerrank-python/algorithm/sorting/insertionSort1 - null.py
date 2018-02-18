# -*- coding: utf-8 -*-
"""insertion sort 1 at hackerrank.com
"""
"""
Input Format 

There will be two lines of input:

s - the size of the array
ar - the sorted array of integers

Output Format 

On each line, output the entire array every time an
item is shifted in it.

Constraints 

1≤s≤1000 
−10000≤V≤10000,V∈ar10
2 3 4 5 6 7 8 9 10 1

Sample Input

5
2 4 6 8 3

Sample Output

2 4 6 8 8 
2 4 6 6 8 
2 4 4 6 8 
2 3 4 6 8 
"""
def insertionSort(ar):    
    
    unsorted = ar[-1]
    
    for i in range(len(ar)-2,-1,-1) : ##reverse traverse a list
        if ar[i] < unsorted :
            ar[i+1] = unsorted
##            print ar[i+1]
            for elem in ar :
                print elem,
            print ''
            break
        ar[i+1] = ar[i]
        for elem in ar :
            print elem,
        if i == 0 :
##            print unsorted
            print ''
            ar[i] = unsorted
            for elem in ar :
                print elem,

        print ''

    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

