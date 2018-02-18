"""Cavity map from hackerrank.com

Problem Statement

You are given a square map of size $n \times n$.
Each cell of the map has a value denoting its depth.
We will call a cell of the map a cavity if and only if this
cell is not on the border of the map and each cell adjacent
to it has strictly smaller depth. Two cells are adjacent if
they have a common side (edge).

You need to find all the cavities on the map and depict them
with the uppercase character X.

:::Input Format:::

The first line contains an integer, $n$, denoting the size of the map.
Each of the following $n$ lines contains $n$ positive digits
without spaces. Each digit (1-9) denotes the
depth of the appropriate area.

Constraints 
$1 \le n \le 100$

:::Output Format:::

Output $n$ lines, denoting the resulting map.
Each cavity should be replaced with character X.

Sample Input

4
1112
1912
1892
1234

Sample Output

1112
1X12
18X2
1234

"""
side = int(raw_input())
grid = []
resGrid = []
for i in range(side) :
    tempRow = raw_input()
    grid.append(tempRow)
#print grid
resGrid.append(grid[0])
for row in range(1,side-1) :
##    print grid[row]
    tempRow = grid[row][0]
    for col in range(1, side-1) :
##        print grid[row][col],
        if int(grid[row][col]) > int(grid[row-1][col]) and \
           int(grid[row][col]) > int(grid[row+1][col]) and \
           int(grid[row][col]) > int(grid[row][col-1]) and \
           int(grid[row][col]) > int(grid[row][col+1]) :
            tempRow += 'X'
        else :
            tempRow += grid[row][col]
    tempRow += grid[row][-1]
    resGrid.append(tempRow)
##    print ''
if side is not 1 :
    resGrid.append(grid[-1])
for i in resGrid :
    print i
