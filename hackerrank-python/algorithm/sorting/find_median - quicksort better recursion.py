"""find median at hackerrank.com
"""
##def partition(array) :
####    global array, size
##    size = len(array)
##    left = []
##    right = []
##    pivotList = []
##    pivot = array[size - 1]
####    pivot = arr[0]
##    for i in array:
##        if i < pivot:
##            left.append(i)
##        elif i > pivot:
##            right.append(i)
##        else:
##            pivotList.append(i)
##    return left, pivotList, right
##
##def quicksort(arr):
##    
##    left = []
##    pivotList = []
##    right = []
##    if len(arr) <= 1:
##        return arr
##    else:
##        left, pivotList, right = partition(arr)
##        left = quicksort(left)
##        right = quicksort(right)
##        return left + pivotList + right
##    

def quicksort(start, stop) :
    global array, half
    if stop - start >= 1:
        pivot = array[stop]
    ##        print pivot, right
        right = None
        for elem in array[start:stop] :
            if elem > pivot :
                right = array.index(elem)
                break
    ##        print right, stop
        if right == None :
            print " ".join(str(i) for i in array)
            quicksort(start, stop - 1)
        else :
            for index in range(right, stop) :
                if array[index] < pivot :
                    array[index], array[right] = array[right], array[index]
                    right += 1
            array[right], array[stop] = array[stop], array[right]
##            print " ".join(str(i) for i in array)
##            print "start, right, stop:\t", start, right, stop 
            if start <= half <= right - 1 :
                quicksort(start, right - 1)
            else : 
                quicksort(right + 1, stop)

size = int(raw_input())
array = [int(elem) for elem in raw_input().strip().split()]
half = size/2
result = quicksort(0, len(array) - 1)
print array[half] 

"""
Problem Statement

In the Quicksort challenges, you sorted an
entire array. Sometimes, you just need specific information about a
list of numbers, and doing a full sort would be
unnecessary. Can you figure out a way to use
your partition code to find the median in an array?

Challenge 
Given a list of numbers, can you find the median?

Input Format 
There will be two lines of input:

n - the size of the array
ar - n numbers that makes up the array
Output Format 
Output one integer, the median.

Constraints

1≤n≤1000001
n is odd
−10000≤x≤10000,x∈ar
Sample Input

7
0 1 2 4 6 5 3
Sample Output

3
"""
