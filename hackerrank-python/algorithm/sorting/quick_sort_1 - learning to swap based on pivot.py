"""quick sort 1 at hackerrank.com
"""
"""
"""
#!/bin/python
def partition(ar):
    p = ar[0]
    for elem in ar[1:] :
        if elem < p :
            ar.remove(elem)
            ar.insert(0,elem)
        else :
            ar.remove(elem)
            ar.insert(-1,elem)
            
    return ""

m = raw_input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
print " ".join(map(str,ar))
