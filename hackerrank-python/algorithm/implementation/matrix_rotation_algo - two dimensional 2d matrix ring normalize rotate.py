"""matrix rotation algo at hackerrank.com
"""
"""
It's okay. The issue is I was using "if var1 is var2 :" instead
of "if var1 == var2 :". 
is keyword works on small values, and doesn't work on strings. What
I didn't know and learnt today was that python modifies large
values so the object doesn't stay the same. That's what I feel happened
here, if you can add to that or have a better hypothesis, please let me know.
"""
def normalizer(start_row, start_col, end_row, end_col, elem_row, elem_col) :
    global times_rotn

    sub_times_rotn = times_rotn
##    print 'In normalizer, row col = ', elem_row, elem_col,
    try : 
        sub_times_rotn = sub_times_rotn % ((end_col - start_col + 1) * 2 + \
                                       (end_row - start_row - 2 + 1) * 2)
##        print sub_times_rotn
    except : 
        print 'zero error at sub_times_rotn =', sub_times_rotn
        
    while sub_times_rotn > 0 :
##        print sub_times_rotn
        if elem_row in (start_row, end_row) and \
           elem_col in (start_col, end_col) :
##            print 'on the edges at', elem_row, elem_col
            if elem_row == start_row :
                if elem_col == start_col :
                    elem_row = elem_row + 1
                else :
                    elem_col = elem_col - 1
            else :
                if elem_col == start_col :
                    elem_col = elem_col + 1
                else :
                    elem_row = elem_row - 1
            sub_times_rotn -= 1
        else :
            shift = 0
##            print elem_row, elem_col, 'and subset', start_row, start_col,
##            print 'upto', end_row, end_col
            if elem_row == start_row :
##                while elem_col is not start_col and sub_times_rotn > 0 : 
##                    elem_col -= 1
##                    sub_times_rotn -= 1
####                print 'elem_row is start_row'
                shift = min(elem_col - start_col, sub_times_rotn)
                elem_col -= shift
            elif elem_row == end_row :
##                while elem_col is not end_col and sub_times_rotn > 0 :
##                    elem_col += 1
##                    sub_times_rotn -= 1
####                print 'elem_row is end_row'
                shift = min(end_col - elem_col, sub_times_rotn)
                elem_col += shift
            elif elem_col == start_col :
##                while elem_row is not end_row and sub_times_rotn > 0 :                
##                    elem_row += 1
##                    sub_times_rotn -= 1
####                print 'elem_col is start_col'
                shift = min(end_row - elem_row, sub_times_rotn)
                elem_row += shift
            else :
##            elif elem_col is end_col :
##                while elem_row is not start_row and sub_times_rotn > 0 :
##                    elem_row -= 1
##                    sub_times_rotn -= 1
####                print 'elem_col is end_col'
                shift = min(elem_row - start_row, sub_times_rotn)
                elem_row -= shift

            sub_times_rotn -= shift
##            print sub_times_rotn
##    print 'turn to', elem_row, elem_col
    return elem_row, elem_col

def rotate_ring(pivot = 0) :
    global mat
    global roted_mat
    global rows, cols
    start_row, start_col = pivot, pivot
    end_row, end_col = rows - pivot, cols - pivot
##    print 'Rows =', start_row, 'upto', end_row
##    print 'Cols =', start_col, 'upto', end_col
    if pivot >= (rows + 1)/2 or pivot >= (cols + 1)/2 :
        return
    for index in range(start_col, end_col + 1) :
        roted_row, roted_col = normalizer(start_row, start_col, \
                                          end_row, end_col, \
                                          start_row, index)
##        print roted_row, roted_col
        roted_mat[roted_row][roted_col] = mat[start_row][index]
        roted_row, roted_col = normalizer(start_row, start_col, \
                                          end_row, end_col, \
                                          end_row, index)
##        print roted_row, roted_col
        roted_mat[roted_row][roted_col] = mat[end_row][index]
    for index in range(start_row + 1, end_row) :
        roted_row, roted_col = normalizer(start_row, start_col, \
                                          end_row, end_col, \
                                          index, start_col)
##        print roted_row, roted_col
        roted_mat[roted_row][roted_col] = mat[index][start_col]
        roted_row, roted_col = normalizer(start_row, start_col, \
                                          end_row, end_col, \
                                          index, end_col)
##        print roted_row, roted_col
        roted_mat[roted_row][roted_col] = mat[index][end_col]
    pivot += 1
    return(rotate_ring(pivot))



rows, cols, times_rotn = map(int, raw_input().split())
rows, cols = rows - 1, cols - 1
mat = tuple([[x for x in raw_input().split()] for y in range(rows + 1)])
roted_mat = [['Fuck' for x in range(cols + 1)] for y in range(rows + 1)]
rotate_ring()
for row in roted_mat :
    print " ".join(row)

"""

Problem Statement


You are given a 2D matrix, a, of dimension MxN and a positive integer R. You have to rotate the matrix R times and print the resultant matrix. Rotation should be in anti-clockwise direction. 

Rotation of a 4x5 matrix is represented by the following figure. Note that in one rotation, you have to shift elements by one step only (refer sample tests for more clarity).

matrix-rotation

It is guaranteed that the minimum of M and N will be even. 

Input 
 First line contains three space separated integers, M, N and R, where M is the number of rows, N is number of columns in matrix, and R is the number of times the matrix has to be rotated. 
 Then M lines follow, where each line contains N space separated positive integers. These M lines represent the matrix. 

Output 
 Print the rotated matrix.

Constraints 
 2 <= M, N <= 300 
 1 <= R <= 109 
 min(M, N) % 2 == 0 
 1 <= aij <= 108, where i ∈ [1..M] & j ∈ [1..N] 

Sample Input #00
4 4 1
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16


Sample Output #00
2 3 4 8
1 7 11 12
5 6 10 16
9 13 14 15


Sample Input #01
4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16


Sample Output #01
3 4 8 12
2 11 10 16
1 7 6 15
5 9 13 14


Sample Input #02
5 4 7
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28


Sample Output #02
28 27 26 25
22 9 15 19
16 8 21 13
10 14 20 7
4 3 2 1


Sample Input #03
2 2 3
1 1
1 1


Sample Output #03
1 1
1 1


Explanation 
Sample Case #00: Here is an illustration of what happens when the matrix is rotated once.
 1  2  3  4      2  3  4  8
 5  6  7  8      1  7 11 12
 9 10 11 12  ->  5  6 10 16
13 14 15 16      9 13 14 15


Sample Case #01: Here is what happens when to the matrix after two rotations.
 1  2  3  4      2  3  4  8      3  4  8 12
 5  6  7  8      1  7 11 12      2 11 10 16
 9 10 11 12  ->  5  6 10 16  ->  1  7  6 15
13 14 15 16      9 13 14 15      5  9 13 14


Sample Case #02: Following are the intermediate states.
1  2  3  4      2  3  4 10    3  4 10 16    4 10 16 22
7  8  9 10      1  9 15 16    2 15 21 22    3 21 20 28
13 14 15 16 ->  7  8 21 22 -> 1  9 20 28 -> 2 15 14 27 ->
19 20 21 22    13 14 20 28    7  8 14 27    1  9  8 26
25 26 27 28    19 25 26 27    13 19 25 26   7 13 19 25



10 16 22 28    16 22 28 27    22 28 27 26    28 27 26 25
 4 20 14 27    10 14  8 26    16  8  9 25    22  9 15 19
 3 21  8 26 ->  4 20  9 25 -> 10 14 15 19 -> 16  8 21 13
 2 15  9 25     3 21 15 19     4 20 21 13    10 14 20  7
 1  7 13 19     2  1  7 13     3  2  1  7     4  3  2  1


Sample Case #03: As all elements are same, any rotation will reflect the same matrix.

"""
"""
def normalizer(start_row, start_col, end_row, end_col, elem_row, elem_col) :
    global times_rotn
    sub_times_rotn = times_rotn
    modder = ((end_col - start_col + 1) * 2 + (end_row - start_row - 2 + 1) * 2)
    if modder == 0 : 
        return elem_row, elem_col
    sub_times_rotn = sub_times_rotn %  modder
##    print 'In normalizer, row col = ', elem_row, elem_col,
    while sub_times_rotn > 0 :
##        print sub_times_rotn
        if elem_row in (start_row, end_row) and \
           elem_col in (start_col, end_col) :
##            print 'on the edges at', elem_row, elem_col
            if elem_row == start_row :
                if elem_col == start_col :
                    elem_row = elem_row + 1
                else :
                    elem_col = elem_col - 1
            else :
                if elem_col == start_col :
                    elem_col = elem_col + 1
                else :
                    elem_row = elem_row - 1
            sub_times_rotn -= 1
        else :
            shift = 0
            if elem_row == start_row :
##                while elem_col is not start_col and sub_times_rotn > 0 : 
##                    elem_col -= 1
##                    sub_times_rotn -= 1
                shift = min(elem_col - start_col, sub_times_rotn)
                elem_col -= shift
            elif elem_row == end_row :
##                while elem_col is not end_col and sub_times_rotn > 0 :
##                    elem_col += 1
##                    sub_times_rotn -= 1
                shift = min(end_col - elem_col, sub_times_rotn)
                elem_col += shift
            elif elem_col == start_col :
##                while elem_row is not end_row and sub_times_rotn > 0 :                
##                    elem_row += 1
##                    sub_times_rotn -= 1
                shift = min(end_row - elem_row, sub_times_rotn)
                elem_row += shift
            else :
##                while elem_row is not start_row and sub_times_rotn > 0 :
##                    elem_row -= 1
##                    sub_times_rotn -= 1
                shift = min(elem_row - start_row, sub_times_rotn)
                elem_row -= shift
            sub_times_rotn -= shift
##    print 'turn to', elem_row, elem_col
    return elem_row, elem_col

def rotate_ring(pivot = 0) :
    global mat
    global roted_mat
    global rows, cols
    start_row, start_col = pivot, pivot
    end_row, end_col = rows - pivot, cols - pivot
##    print 'Rows =', start_row, 'upto', end_row
##    print 'Cols =', start_col, 'upto', end_col
    if pivot >= (rows + 1)/2 or pivot >= (cols + 1)/2 :
        return
    for index in range(start_col, end_col + 1) :
        roted_row, roted_col = normalizer(start_row, start_col, \
                                          end_row, end_col, \
                                          start_row, index)
##        print roted_row, roted_col
        roted_mat[roted_row][roted_col] = mat[start_row][index]
        roted_row, roted_col = normalizer(start_row, start_col, \
                                          end_row, end_col, \
                                          end_row, index)
##        print roted_row, roted_col
        roted_mat[roted_row][roted_col] = mat[end_row][index]
    for index in range(start_row + 1, end_row) :
        roted_row, roted_col = normalizer(start_row, start_col, \
                                          end_row, end_col, \
                                          index, start_col)
##        print roted_row, roted_col
        roted_mat[roted_row][roted_col] = mat[index][start_col]
        roted_row, roted_col = normalizer(start_row, start_col, \
                                          end_row, end_col, \
                                          index, end_col)
##        print roted_row, roted_col
        roted_mat[roted_row][roted_col] = mat[index][end_col]
    pivot += 1
    return(rotate_ring(pivot))



rows, cols, times_rotn = map(int, raw_input().split())
rows, cols = rows - 1, cols - 1
mat = tuple([[x for x in raw_input().split()] for y in range(rows + 1)])
roted_mat = [['0' for x in range(cols + 1)] for y in range(rows + 1)]
rotate_ring()
for row in roted_mat :
    print " ".join(row)
    """
##above we have a fully working code!
