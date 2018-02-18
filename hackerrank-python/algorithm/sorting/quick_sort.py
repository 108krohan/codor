def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        for i in less :
            print i,
        for i in pivotList :
            print i,
        for i in more :
            print i,
        print ''
        return less + pivotList + more
 
##a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
size = int(raw_input())
a = [int(x) for x in raw_input().strip().split()]
##print a
a= quickSort(a)
