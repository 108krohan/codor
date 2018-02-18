"""degree of dirtiness at hackerrank.com
"""
def find_min(half, len_half) :
##    global len_half
    index = len_half - 1 
    minimum = half[index]
    try : 
        while minimum == half[index] :
            index -= 1
        return index + 1, False
    except :
        return 0, True
        

def action(half, comes_from = 'left') :
    global position, num_toilets, Mth, dirtiness
##    minimum = min(half)
##    index = half.index(minimum)
    len_half = len(half)
    index, zero = find_min(half, len_half)
##    print index,
##    if zero : 
    if comes_from == 'left' :
        position = index
        if zero :
            position += 1
    else : 
        position = num_toilets - (index)    
    half[index] += 1
    dirtiness = half[index]
##    else :
##        if comes_from == 'left' :
##            position = index
##        else : 
##            position = num_toilets - (index)    
##        half[index] += 1
##        dirtiness = half[index]        
##    print comes_from, half 
            
    
##def find_toilet() :
##    global left, right
##    action(left)
##    action(right, 'right')

def first_time(upto, limit) :
    global left, right, position
    count = 0
    index = 1
    while True :
        if count < upto :
            left.append(0)
            count += 1
            position = index
##            print 'left add'
        if count == upto or count == limit :
            break
        if count < upto :
            right.append(0)
            count += 1
##            print 'right add'
            position = upto - index
        index += 1
##        print 'index =', index
        if count == upto or count == limit :
            break
##    print left, right
    return count


testcases = int(raw_input())
for _ in range(testcases) :
    num_toilets, Mth = map(int, raw_input().split())
    position = 0
    dirtiness = 0
    if num_toilets == 1 :
        position = 1
        dirtiness = Mth - 1
        print position, dirtiness
        continue
            
##    left = [0 for i in range(num_toilets/2 + (num_toilets)%2)]
##    right = [0 for i in range(num_toilets/2)]
##    print left, right
    left, right = [], []
    count = first_time(num_toilets, Mth)
##    print count
    if count == num_toilets :
        if num_toilets % 2 == 0 : 
            for man in range(1, Mth - count, 2) :
        ##        find_toilet()
                action(left)
                action(right, 'right')        
            if Mth % 2 != 0 :
                print left, right
                action(left)
        else :
            for man in range(1, Mth - count, 2) :
        ##        find_toilet()
                action(right, 'right')
                action(left)
            if Mth % 2 == 0 :
                action(right, 'right')
    print position, dirtiness

"""
Problem Statement

There are N toilets in a row indexed from 1 to N. At a time, 2 people enter the washroom. The degree of dirtiness of each toilet is 0 initially and it increases by 1 after it is used each time. The 1st person occupies the 1st toilet with the lowest degree of dirtiness moving from 1 to N. The 2nd person occupies the toilet with the lowest degree of dirtiness moving from N to 1. The next two people enter the toilet when the first two people have left. Find the index of toilet and degree of dirtiness for the Mth person.

Note In case M is odd, the last person walks into the washroom alone and occupies the least dirty toilet moving from 1 to N.

Input Format 
The first line contains T, the number of test cases. Each test case consists of one line containing N, the number of toliets, and M, the person to enter the toilet, seperated by space.

Output Format 
The index of the toilet used by M and its degree of dirtiness D.

Constraints 
1≤T≤10 
1≤N≤50000 
1≤M≤106

Sample Input

3  
10 3  
5 8  
4 26 
Sample Output

2 0  
4 1  
4 6  
Explanation

In the second test case, 
for the first two persons, positions are 1 _ _ _ 2, degree of dirtiness 0 0 0 0 0 (dirtiness is 0 since they are the first to use it) 
for person 3 and 4, positions are _ 3 _ 4 _ , degree of dirtiness 1 0 0 0 1 
for 5 and 6, positions are _ _ 5 _ 6, degree of dirtiness 1 1 0 1 1 
for 7 and 8, positions are 7 _ _ 8 _, degree of dirtiness 1 1 1 1 2 so the answer is 4,1
"""
