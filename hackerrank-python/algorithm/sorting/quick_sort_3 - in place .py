"""quick sort 3 at hackerrank.com
"""
def quicksort():
    _quicksort(0, len(array) - 1)

"""following is the algorithm for lomuto partioning that hackerrank demanded
I use."""
def _quicksort(start, stop) :
    global array
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
            _quicksort(start, stop - 1)
        else :
            for index in range(right, stop) :
                if array[index] < pivot :
                    array[index], array[right] = array[right], array[index]
                    right += 1
            array[right], array[stop] = array[stop], array[right]
            print " ".join(str(i) for i in array)
##            print "start, right, stop:\t", start, right, stop 
            _quicksort(start, right - 1)
            _quicksort(right + 1, stop)

size = int(raw_input())
array = [int(i) for i in raw_input().strip().split()]
##_quicksort(array)
length = len(array)
quicksort()


"""copied from wikipedia/algorithms for quick sort.
It's a wonderful algorithm and better than the one above.
However, for understanding, the above code works flawlessley
"""
##def _quicksort(array, start, stop):
##    if stop - start > 0:
##        pivot, left, right = array[stop], start, stop
##        while left <= right:
##            while array[left] < pivot:
##                left += 1
##            while array[right] > pivot:
##                right -= 1
##            if left <= right:
##                array[left], array[right] = array[right], array[left]
##                left += 1
##                right -= 1
##        print array
##        _quicksort(array, start, right)
##        _quicksort(array, left, stop)
