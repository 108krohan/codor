"""Efficiency, Order of Growth, and Computational Complexity.
Recursive searching via binary method.
"""


def f(n):
    assert n >= 0
    answer = 1
    while n > 1 :
        answer *= n
        n -= 1
    return answer

def search(L,e):
    for elem in L :
        if elem == e :
            return True
        if elem > e :
            return False
    return False



def bSearch(L,e,low,high):
    global numCalls
    numCalls += 1
    if high - low < 2 :
        return L[low] == e or L[high] == e
    mid = low + int ((high - low)/2)
    if L[mid] == e :
        return True
    if L[mid] > e :
        return bSearch(L,e,low,mid-1)
    else :
        return bSearch(L,e,mid+1,high)

numCalls = 0
L = [1,2,3,3,5,5,17,28,44,77,87,88,96,100]    
print bSearch(L,16,0,len(L)-1)
print bSearch(L,28,0,len(L)-1)
