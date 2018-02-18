"""the maximum subarray at hackerrank.com
"""
"""
"""


def findContig(array, size) :

    current_sum = 0
    current_index = -1
    best_sum = 0
    best_start_index = -1
    best_end_index = -1
    
    for index in xrange(size) :
        val = current_sum + array[index]

        if val > 0 :
            if current_sum == 0 :
                current_index = index
            current_sum = val
        else :
            current_sum = 0

        if current_sum > best_sum :
            best_sum = current_sum
            best_start_index = current_index
            best_end_index = index
    return best_sum
    

    
cases = int(raw_input())

for _ in range(cases) :

    size = int(raw_input())
    array = [int(elem) for elem in raw_input().split()]

    contig = 0
    nonContig = 0
    possContigAddn = 0
    newContig = 0
    
    maxima = array[0]

##    for index in range(size) :
##
##        possContig += array[index]
##        try :
##
##            if possContig > 0 :
##                possContig, contig = 0, possContig + contig
##                    
##            if array[index] > 0 :
##                nonContig += array[index]
##            if array[index] > maxima :
##                maxima = array[index]
##        except IndexError:
##                pass
    nothing = True
    for index in range(size) :
        if array[index] > maxima :
            nothing = False
            maxima = array[index]
        if array[index] > 0 :
            nonContig += array[index]

    if nothing :
        print maxima, maxima

    else :
        contig = findContig(array, size)
        print contig, nonContig
