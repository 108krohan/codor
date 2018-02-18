"""quick sort 2 at hackerrank.com
"""

##def quickSort(arr):
##    less = []
##    pivotList = []
##    more = []
##    if len(arr) <= 1:
##        return arr
##    else:
##        pivot = arr[0]
##        for i in arr:
##            if i < pivot:
##                less.append(i)
##            elif i > pivot:
##                more.append(i)
##            else:
##                pivotList.append(i)
##        less = quickSort(less)
##        more = quickSort(more)
##        for i in less :
##            print i,
##        for i in pivotList :
##            print i,
##        for i in more :
##            print i,
##        print ''
##        return less + pivotList + more
## 
####a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
##size = int(raw_input())
##a = [int(x) for x in raw_input().strip().split()]
####print a
##a= quickSort(a)


"""better quicksort new array method
"""
def partition(array) :
##    global array, size
    size = len(array)
    left = []
    right = []
    pivotList = []
    pivot = array[size - 1]
##    pivot = arr[0]
    for i in array:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            pivotList.append(i)
    return left, pivotList, right

def quicksort(arr):
    left = []
    pivotList = []
    right = []
    if len(arr) <= 1:
        return arr
    else:
        left, pivotList, right = partition(arr)
        left = quicksort(left)
        right = quicksort(right)
        return left + pivotList + right
    

size = int(raw_input())
array = [int(elem) for elem in raw_input().strip().split()]
half = size/2
result = quicksort(array)
print result

