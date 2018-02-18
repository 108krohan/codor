"""running time quicksort at hackerrank.com
"""
"""
General summary : Use quicksort via lomuto partitioning and insertion sort.
"""

def _quicksort(start, stop) :
    global array
    global _quicksort_count
    if stop - start >= 1:
        pivot = array[stop]
        right = None
        for elem in array[start:stop] :
            if elem > pivot :
                right = array.index(elem)
                break
            _quicksort_count += 1
        if right == None :
##            print " ".join(str(i) for i in array)
            _quicksort_count += 1
            _quicksort(start, stop - 1)
        else :
            for index in range(right, stop) :
                if array[index] < pivot :
                    array[index], array[right] = array[right], array[index]
                    _quicksort_count += 1
                    right += 1
            array[right], array[stop] = array[stop], array[right]
##            print " ".join(str(i) for i in array)
            _quicksort_count += 1
            _quicksort(start, right - 1)
            _quicksort(right + 1, stop)

            
def _insertionsort(arr, start, stop) : 
    global _insertionsort_count
    for index in range(start, stop + 1) :
        sub_index = index - 1
        while arr[sub_index] > arr[sub_index + 1] and sub_index >= 0:
            arr[sub_index], arr[sub_index + 1] = arr[sub_index + 1], \
                                                 arr[sub_index]
            sub_index -= 1
            _insertionsort_count += 1
##    print arr    

_quicksort_count = 0
_insertionsort_count = 0
size = int(raw_input())
array = [int(i) for i in raw_input().strip().split()]
arr = array[:]
_quicksort(0, len(array) - 1)
_insertionsort(arr, 0, len(array) - 1)
print _insertionsort_count, _quicksort_count
