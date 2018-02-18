"""almost sorted at hackerrank.com"""

def check_swap(first_index) :
    """checks if a swap can fix an issue!"""
    global array
    index = first_index - 1
    try :
        while not((index == 0 or array[index - 1] < array[first_index]) and \
              (array[index + 1] >= array[first_index])) :
            index -= 1
        array[index], array[first_index] = array[first_index], array[index]    
        if check_sorted() :
            return index + 1, True
        else :
            return None, False
    except :
        return None, False
    
global size
def check_reverse(first_index) :
    """checks if array can be fixed by a reverse!"""
    global array
    index = first_index
    try :
        while array[index] > arry[index + 1] :
            index += 1
    except :
        return size - 1, True
    if check_sorted(index) :
        return index, True
    else :
        return None, False
    
def check_sorted(first_index = 0, last_index = None ) :
    """checks if in ascending order!"""
    if last_index == None :
        last_index = size - 1
    global array
    try :
        while array[first_index] <= array[last_index] :
            first_index += 1
        return False
    except :
        return True
size = int(raw_input())
array = [int(i) for i in raw_input().split()]
aready_sorted = False
index = 0
##finding the first anomaly!
try : 
    while array[index] <= array[index + 1] :
        index += 1    
except :
    ##already sorted!
    print 'yes'
    already_sorted = True
    
first_index = index
##if 1 2 4 6 3, then index of 6 will be considered.
##finding upto_what_anomaly!
try :
    while array[index] > array[index + 1] :
        index += 1
except :
    index = size - 1

last_index = index
##if next item is the only anomaly!
if last_index == first_index + 1 :
##saying that : 1 2 4 6 3 4 - first_index = [6], last_index = [3]
    last_index, test = check_swap(first_index + 1)
    if test :
        print 'yes'
        print 'swap', last_index, first_index + 2
    else :
        print 'no'
else :
    ##if the anomaly is long
    last_index, test = check_reverse(first_index)
    if test :
        print 'yes'
        print 'reverse', first_index + 1, last_index
    else :
        print 'no'
        

"""Problem Statement

Given an array with n elements, can you sort this array in ascending order using only one of the following operations?

Swap two elements.
Reverse one sub-segment.
Input Format 
The first line contains a single integer, n, which indicates the size of the array. 
The next line contains n integers separated by spaces.

n  
d1 d2 ... dn  
Constraints 
2≤n≤100000 
0≤di ≤1000000 
All di are distinct.

Output Format 
1. If the array is already sorted, output yes on the first line. You do not need to output anything else.

If you can sort this array using one single operation (from the two permitted operations) then output yes on the first line and then:

a. If you can sort the array by swapping dl and dr, output swap l r in the second line. l and r are the indices of the elements to be swapped, assuming that the array is indexed from 1 to n.

b. Else if it is possible to sort the array by reversing the segment d[l...r], output reverse l r in the second line. l and r are the indices of the first and last elements of the subsequence to be reversed, assuming that the array is indexed from 1 to n.

d[l...r] represents the sub-sequence of the array, beginning at index l and ending at index r, both inclusive.

If an array can be sorted by either swapping or reversing, stick to the swap-based method.

If you cannot sort the array in either of the above ways, output no in the first line.

Sample Input #1

2  
4 2  
Sample Output #1

yes  
swap 1 2
Sample Input #2

3
3 1 2
Sample Output #2

no
Sample Input #3

6
1 5 4 3 2 6
Sample Output #3

yes
reverse 2 5
Explanation 
For #1, you can both swap(1, 2) and reverse(1, 2), but if you can sort the array using swap, output swap only. 
For #2, it is impossible to sort by one single operation (among those permitted). 
For #3, you can reverse the sub-array d[2...5] = "5 4 3 2", then the array becomes sorted."""
