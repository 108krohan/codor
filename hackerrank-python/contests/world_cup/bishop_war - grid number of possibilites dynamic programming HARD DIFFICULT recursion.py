"""bishop war at hackerrank.com"""

def fillbar(donebar, thisrow, thiscol) :
    """fill the chess mould with hashtags to damaged active sites"""
    """always goes down in diagonal and anti diagonal"""
    global row, col
    funbar = []
    for elem in donebar[1:] :
        funbar.append(elem[:])
    drow, dcol, adrow, adcol = 0, thiscol + 1, 0, thiscol - 1
##    print '\n'.join([''.join(i) for i in funbar])
##    print ''
    while drow < row - thisrow - 1 and dcol < col and funbar[drow][dcol] != '*' :
        ##diagonal
        funbar[drow][dcol] = '#'
        drow += 1
        dcol += 1
    while adrow < row - thisrow - 1 and adcol >= 0 and funbar[adrow][adcol] != '*':
        ##antidiagonal
        funbar[adrow][adcol] = '#'
        adrow += 1
        adcol -= 1
    return funbar
##num_store = [[None]*10 for _ in xrange(10)]
def next_row(donebar, thisrow = 0) :
    """goes row by row in the chess mould, extracting points by points till"""
    """it reaches the bottom"""
    global row, col
    if thisrow == row - 1 :
        return donebar[0].count('.')
    answer = 0
    if donebar[0].count('.') == 0 :
        return
    for thiscol in xrange(col) :
        if donebar[0][thiscol] == '.' :
            new_grid = fillbar(donebar, thisrow, thiscol)
            result = next_row(new_grid, thisrow + 1)
##            num_store[thisrow][thiscol] = 
            if result != None :                
                answer += result
    return answer



row, col = map(int, raw_input().split())
grid = [list(raw_input()) for _ in xrange(row)]
##for elem in grid :
##    print ''.join(elem)
##print '-'*10
result = next_row(grid)
print result 




##def fillbar(donebar, thisrow, thiscol) :
##    """fill the chess mould with hashtags to damaged active sites"""
##    """always goes down in diagonal and anti diagonal"""
##    global row, col
##    funbar = donebar[:thisrow + 1]
##    for elem in donebar[thisrow:] :
##        funbar.append(elem[:])
##    drow, dcol, adrow, adcol = thisrow + 1, thiscol + 1, thisrow + 1, thiscol - 1
##    while drow < row and dcol < col and funbar[drow][dcol] != '*' :
##        ##diagonal
##        funbar[drow][dcol] = '#'
##        drow += 1
##        dcol += 1
##    while adrow < row and adcol >= 0 and funbar[adrow][adcol] != '*':
##        ##antidiagonal
##        funbar[adrow][adcol] = '#'
##        adrow += 1
##        adcol -= 1
####    print '-/'*10, thisrow + 1, '\-'*10
####    for elem in funbar :
####        print ' '*10*thisrow, ''.join(elem)
####    funbar.extend(donebar[row_index:])
##    
##    return funbar
##
##def next_row(donebar, thisrow = 0) :
##
##    """goes row by row in the chess mould, extracting points by points till"""
##    """it reaches the bottom"""
##
##    global row, col
##    if thisrow == row - 1 :
##        return donebar[row - 1].count('.')
##
##    answer = 0
##
##    if donebar[thisrow].count('.') == 0 :
##        return
##
##    for thiscol in xrange(col) :
##        if donebar[thisrow][thiscol] == '.' :
##            new_grid = fillbar(donebar, thisrow, thiscol)
##            result = next_row(new_grid, thisrow + 1)
##            if result != None : 
##                answer += result
####                print answer
##    return answer
##
##
##row, col = map(int, raw_input().split())
##grid = [list(raw_input()) for _ in xrange(row)] ##don't turn each elem inside a list, HUGE prob.
####for elem in grid :
####    print ''.join(elem)
####print '-'*10
##result = next_row(grid)
##print result 


##rewriting the fillbar function, owing to change of inside elements back to string!!
##
##def fillbar(donebar, thisrow, thiscol) :
##    """fill the chess mould with hashtags to damaged active sites"""
##    """always goes down in diagonal and anti diagonal"""
##
##    global row, col
##    funbar = donebar[:thisrow]
##    dcol, adcol = thiscol + 1, thiscol - 1
##    new_row = thisrow + 1
##    funbar = donebar[:thisrow + 1]
##    ad_blocked = False
##    d_blocked = False
##    total_blocked = False
##    while new_row < row and dcol < col and adcol >= 0 :
##        if donebar[new_row][adcol] == '*' and donebar[new_row][dcol] == '*' :
##            total_block = True
##        if donebar[new_row][adcol] == '*' :
##            ad_blocked = True
##            break
##        if donebar[new_row][dcol] == '*' :
##            d_blocked = True
##            break
##        onebar = donebar[new_row][:adcol] + '#' + donebar[new_row][adcol + 1: dcol] + \
##                 '#' + donebar[new_row][dcol + 1: ]
##        dcol += 1
##        adcol -= 1
##        funbar.append(onebar)
##        new_row += 1
##    if not total_blocked :     
##        if adcol < 0 or ad_blocked :
##            while dcol < col and new_row < row :
##                if donebar[new_row][dcol] == '*' :
##                    break
##                onebar = donebar[new_row][:dcol] + '#' + donebar[new_row][dcol + 1:]
##                new_row += 1
##                dcol += 1
##                funbar.append(onebar)
##
##        if dcol >= col or d_blocked :
##            while adcol >= 0 and new_row < row :
##                if donebar[new_row][adcol] == '*' :
##                    break
##                onebar = donebar[new_row][:adcol] + '#' + donebar[new_row][adcol + 1:]
##                new_row += 1
##                funbar.append(onebar)
##                adcol -= 1
##
##    funbar.extend(donebar[new_row:])
####    print '-/'*10, thisrow + 1, '\-'*10
####    for elem in funbar :
####        print ' '*10*thisrow, ''.join(elem)
##    return funbar


"""
Problem Statement

You are given a board with N rows and M columns. In this board you have to place exactly 1 bishop in each row. There are also some obstacles in some of the cells where you can't place a bishop. Bishops can only move diagonally but they can't go to a cell where there is any obstacle. Two bishops can attack each other if one of them can move to the cell of the other bishop. Now you have to count the number of ways that you can place bishops in the board.

Note: Two bishops can attack each other if one of them can move to the cell of the other bishop in a single move without passing any obstacles.

Input Format

The first line of the input contains two integers N and M. The following N lines contain M characters each, the description of the board. Each cell of the board is either '.' which means that this cell is free or '*' which means that this cell contains an obstacle.

Constraints

1<=N,M<=10

Output Format

Print only one integer representing the number of ways to put exactly one bishop in each row such that no two bishops attack each other.

Sample Input

3 3
..*
.**
.*.

Sample Output

2

Explanation

Two ways of placing would be:

B.*
B**
B*.

and ..

B.*
B**
.*B

Here B means a bishop.
"""
