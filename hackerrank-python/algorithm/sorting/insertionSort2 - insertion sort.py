"""insertion sort 2 at hackerrank.com
"""
"""
Sample Input

6
1 4 3 5 6 2
Sample Output

1 4 3 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 2 3 4 5 6 
"""
def insertionSort(ar):


    for i in range(1,len(ar)) :
        icopy = i
        while (ar[icopy] < ar[icopy-1]) and icopy > 0 :
            ar[icopy], ar[icopy - 1] = ar[icopy - 1], ar[icopy]
            icopy -= 1
        for elem in ar :
            print elem,
        print ''
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
