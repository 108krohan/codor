"""
"""
"""
"""
def insertion_sort(l):
    count = 0
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           count += 1
           j -= 1
        l[j+1] = key
    print count

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
##print " ".join(map(str,ar)) ##sexy way to print
