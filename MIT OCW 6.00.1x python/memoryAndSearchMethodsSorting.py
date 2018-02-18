"""Recorded lecture 9.
=Selection sort
=Merge sort
=String Merge sort
=Function within function
"""
##
####Selection Sort
##def selSort(L):
##    ##ascending order
##    for i in range (len(L)-1):
##        ##Invariant : the list L[:] is sorted
##        minIndex = i
##        minVal = L[i]
##        j = i + 1
##        while j < len(L) :
##            if minVal > L[j]:
##                minIndex = j
##                minVal = L[j]
##            j += 1
##        temp = L[i]
##        L[i] = L[minIndex]
##        L[minIndex] = temp
##        print 'partially sorted list = ', L
## 
##L = [35, 4, 5, 29, 17, 58, 0]
##selSort(L)
##print 'Sorted List = ', L
##


"""merge sort techinque"""
def merge (left, right, lt):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if lt(left[i], right[j]) :
            result.append(left[i])
##            print 'merging ', left[i],  result
            i += 1
        else :
            result.append(right[j])
            j += 1
##            print 'merging ', right[i], result
    while i < len(left) :
        result.append(left[i])
        i += 1
    while j < len(right) :
        result.append(right[j])
        j += 1
    return result

def sort (L, lt = lambda x,y : x < y):
    if len(L) < 2 :
        return L[:]
    else :
        middle = int(len(L)/2)
        left = sort (L[:middle],lt)
        right = sort (L[middle:],lt)
        print 'About to merge', left, 'and', right
        return merge (left, right, lt)

##L = [35, 4, 5, 29, 17, 58, 0]
##newL = sort(L)
##print 'SortedList = ', newL
##L = [1.0, 2.25, 24.5, 12.0, 2.0, 23.0, 19.125, 1.0]
##newL = sort(L, float.__lt__) ##gt descending order
##print 'SortedList = ', newL

"""lastname and first name"""
###use this program with the merge sort function given above.
def lastNameFirstName(name1,name2):
    import string
    name1 = string.split(name1, ' ')
    name2 = string.split(name2, ' ')
    if name1[1] is not name2[1] :
        return name1[1] < name2[1]
    else :
        return name1[0] < name2[0]

def firstNameLastName (name1, name2) :
    import string
    name1 = string.split (name1, ' ')
    name2 = string.split (name2, ' ')
    if name1[0] is not name2[0] :
        return name1[0] < name2[0]
    else :
        return name1[1] < name2[0]

L = ["John Guttag", "Ronit Kumar", "Rohan Awesome Kumar", "Kanishka Kumar", \
     "Taurooshya Yadav"]
newL = sort(L, lastNameFirstName) ##acts as lt now, for strings.
print 'SortedList = ', newL



