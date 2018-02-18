"""grid maze at 101hack August at hackerrank.com
"""

def path_taken(x, y, dx, dy) :
    global grid, walls, P_row, P_col

    new_cord = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    dist = 999
    for cord in new_cord :
        try :
            x, y = new_cord[0], new_cord[1]
            if grid[x][y] == 'P' :
                print walls
                return 
            if grid[x][y] == '.' :
                dist = min(found_dot(x, y), dist)
            

rows, cols = map(int, raw_input().split())

##grid = [ raw_input() for i in range(rows)]
P_found = False
grid = []
P_col, P_row, S_col, S_row = 0,0,0,0
for index in range(rows) :
    one_row = raw_input()
    if P_found and 'P' in one_row :
        P_col = one_row.index('P')
        P_row = index
    if S_found and 'S' in one_row :
        S_col = one_row.index('S')
        S_row = index
    grid.append(one_row)

disx = P_col - S_col
if disx > 0 :
    dx = 1
else :
    dx = -1
disy = P_row - S_row
if disy > 0 :
    dy = 1
else :
    disy = -1
walls = 0
path_taken(S_col, S_row, dx, dy)


"""
Problem Statement

Mika and Zloba love grid mazes. A grid maze is an n×m rectangle maze where each cell is either empty, or is a wall. Let us denote the cell at the intersection of i-th line and j-th column (i,j). In any moment, our friend can move from one cell to another only if both cells are empty and have a common side. So, from empty cell (i,j), they can move to empty cells (i−1,j), (i,j−1), (i,j+1), and (i+1,j). But this may not be so easy. Sometimes there is a lot of walls and way between two cells doesn't exist. In this case we should break some walls (if we break a wall, the cell containing the wall becomes empty).

At the beginning Mika and Zloba are located at the empty cell S. They must go for their supply located at the empty cell P and after that get out of the maze. We consider that they got out of the maze only if they are located at cell on the border of the maze.

We all like our heroes and we want to help them. Find the minimum number of walls needed to be broken so that Mika and Zloba can complete their journey.

Input Format

The first line contains two numbers n and m (1≤n,m≤1000), where n and m are the maze's height and width.

Each of the next n lines contains m characters. They describe the maze: the character at the intersection of i-th line and j-th column is equal to value of cell (i,j). Cell can have values ".", "#", S, and P, where "." denotes empty cell, "#" denotes cell containing wall, and S and P are empty points, vital for our heroes as described in the statement. It is guaranteed that there will be exactly one cell with value S and exactly one cell with value P in the maze.

Output Format

In the single line print one number - minimum number of walls needed to be broken so that Mika and Zloba can move from cell S to cell P and after that get out of the maze.

Sample Input 1:

5 6
##..##
######
S#####
##P##.
###..#
Sample Output 1:

2
Sample Input 2:

4 4
...#
#P.#
##.#
.#S.
Sample Output 2:
0
Explanation

In the first sample maze's height is 5 and maze's width is 6. Mika and Zloba are located at the cell (3,1) and supply is located at cell (4,3). They must break at least two walls. One of the optimal options is to break the wall on cell (3,2), and break the wall on cell (3,3). Now they can go to P and after that they can return using the same path to S and then get out of the maze. So, the answer is 2.

In the second sample they don't need to break any wall at all. They can choose the following path: (4,3)−(3,3)−(2,3)−(2,2)−(1,2) - leave the maze. The answer is 0.
"""
