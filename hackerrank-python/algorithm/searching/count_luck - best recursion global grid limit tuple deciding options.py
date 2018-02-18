"""count luck at hackerrank.com
"""

global limit
global grid
def path_taken(current_pos, back = (), waved_wand = 0) :
    global limit
    global grid
    row = current_pos[0]
    col = current_pos[1]
    options = []
##    print current_pos
    found_exit = False
    new_coordinates = ((row - 1, col), (row + 1, col), (row, col + 1), \
                  (row, col - 1))
    for new_position in new_coordinates :
        if new_position != back :
            new_row, new_col = new_position[0], new_position[1]
            if 0 <= new_row < limit[0] and 0 <= new_col < limit[1] :
##                print new_row, new_col
##                if grid[new_row][new_col] == 'X' :
##                    pass        ##this is unnecessary.
                if grid[new_row][new_col] == '*' :
                    found_exit = True
##                        return waved_wand  ##this is wrong.
##"""currently we've only seen what's in this perspective.
##We have not yet stepped on the exit... If there are more options,
##Hermione will have to wave her wand one more final time before stepping
##on the exit."""
                elif grid[new_row][new_col] == '.' :
                    options.append((new_row, new_col))
##    print options
##"""this is what I'm talking about. Added a flag and then final check is done
##for all the options. If there are options, then a wand is waved."""
    if found_exit :
        if options == [] :
            return waved_wand
        else :
            return waved_wand + 1
    if options == [] :
        pass
    elif len(options) == 1 :
        return path_taken(options[0], current_pos, waved_wand)
    else :
        waved_wand += 1
        for one_option in options :
            one_path = path_taken(one_option, current_pos, waved_wand)
            if one_path == None :
                continue
            else :
                return one_path

testcases = int(raw_input())
for _ in range(testcases) :
    num_str, size_str = [int(i) for i in raw_input().split()]
    global limit
    global grid
    limit = num_str, size_str
    grid = [raw_input() for i in range(num_str)]
    K = int(raw_input())
##    print grid
    marker = 0, 0
    for one_row in range(num_str) :
        for one_col in range(size_str) :
            if grid[one_row][one_col] == 'M' :
                marker = one_row, one_col
##    print marker     
    wand_waves = path_taken(marker, grid)
    if wand_waves == K :
        print 'Impressed', wand_waves, K
    else :
        print 'Oops!', wand_waves, K

"""alternate path_taken function for the program.
This doesn't make the grid global.
##import sys
##sys.setrecursionlimit(2000)
##global limit
##def path_taken(current_pos, grid, back = (), waved_wand = 0) :
##    global limit
##    row = current_pos[0]
##    col = current_pos[1]
##    options = []
####    print current_pos
##    new_coordinates = ((row - 1, col), (row + 1, col), (row, col + 1), \
##                  (row, col - 1))
##    for new_position in new_coordinates :
##        if new_position != back :
##            new_row, new_col = new_position[0], new_position[1]
##            if 0 <= new_row < limit[0] and 0 <= new_col < limit[1] :
####                print new_row, new_col
####                if grid[new_row][new_col] == 'X' :
####                    pass        
##                if grid[new_row][new_col] == '*' :
####                    print grid[new_row][new_col]
##                    return waved_wand
##                elif grid[new_row][new_col] == '.' :
##                    options.append((new_row, new_col))
####    print options
##    if len(options) == [] :
##        return
##    elif len(options) == 1 :
##        return path_taken(options[0], grid, current_pos, waved_wand)
##    else :
##        waved_wand += 1
####        print 'waved_wand =', waved_wand
##        for one_option in options :
##            one_path = path_taken(one_option, grid, current_pos, waved_wand)
##            if one_path == None :
##                continue
##            else :
##                return one_path
"""


"""
Problem Statement

Hermione Granger is lost in the Forbidden Forest while collecting
some herbs for a magical potion. The forest is magical and
has only one exit point, which magically transports her back to
the Hogwarts School of Witchcraft and Wizardry. 
The forest can be considered as a grid of N×M size. Each
cell in the forest is either empty (represented by '.') or
has a tree (represented by 'X'). Hermione can
move through empty cells, but not through
cells with a tree in it. She can
only travel LEFT, RIGHT, UP, and DOWN. Her position in the forest is
indicated by the marker 'M' and the location of the exit
point is indicated by '*'. Top-left corner is indexed (0, 0).

.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
In the above forest, Hermione is located
at index (2, 7) and the exit is at (1, 2). Each cell is
indexed according to Matrix Convention

She starts her commute back to the exit, and every time she encounters
more than one option to move, she waves her wand and the
correct path is illuminated and she proceeds in
that way. It is guaranteed that there is only one path to
each reachable cell from the starting cell. Can you tell
us if she waved her wand exactly K times or not?
Ron will be impressed if she is able to do so.

Input Format 

The first line contains an integer T; T test cases follow. 
Each test case starts with two space-separated integers, N and M. 
The next N lines contain a string, each having a length of M,
which represents the forest. 
The last line of each single test case contains integer K.

Output Format 
For each test case, if she could impress Ron then
print Impressed, otherwise print Oops!.

Constraints 
1≤T≤10 
1≤N,M≤100 
0≤K≤10000 
There is exactly one 'M' and one '*' in the graph. 
Exactly one path exists between 'M' and '*.'

Sample Input

3
2 3
*.M
.X.
1
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
3
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
4
Sample Output

Impressed
Impressed
Oops!
Explanation

Case 1: Hermione waves her wand at (0,2), hence #Wand waved = K = 1. 
Case 2: Hermione waves her wand at (2,9) (0,5), and (3,3), hence
#Wand waved = K = 3. 
Case 3: Same as above. But here K = 4, which doesn't
match the number of times her wand is waved.
"""
"""
Input parameters and output parameters
6
3 41
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
M.......................................*
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
20
5 11
..........*
.XXXXXXXXXX
...........
XXXXXXXXXX.
M..........
0
5 17
XXXXXXXXXXXXXXXXX
XXX.XX.XXXXXXXXXX
XX.*..M.XXXXXXXXX
XXX.XX.XXXXXXXXXX
XXXXXXXXXXXXXXXXX
1
41 41
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
M........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.*.......................................
280
5 17
XXXXXXXXXXXXXXXXX
XXX.XX.XXXXXXXXXX
XX.*..M.XXXXXXXXX
XXX.XX.XXXXXXXXXX
XXXXXXXXXXXXXXXXX
10
41 41
.X.XXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.
...XXXXXXXXXXXXXXXXXXX...................
.X..X.X.X.X.X.X.X..XXXX*X.X.X.X.X.X.X.XX.
.XXXX.X.X.X.X.X.X.XX.X.X.X.X.X.X.X.X.X.X.
.........................................
.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XX.X.X.X.XX.X.XX.X.X.X.X.X.X.X.X.X.X.X.X
.X.X.X.X.X.XXX.X.X.X.X.X.X.X.X.X.X.X.X.X.
X........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.X.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.XX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XMX.
.X....................................X..
..X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.X...................................X...
.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.XX.XXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
294

Impressed
Impressed
Impressed
Impressed
Oops!
Impressed
++++++++++++++++++++++++++++++++++++++++++

9
37 31
X.XXXX.XX....X.XX...X.XXXXXXXXX
X.XXX...XXX.X..XXX.XX..XXXXXXXX
...X.XX..X...X..XX.X..XXXXXXXXX
X.X..X..X.X.X..X.....XX.XXXXXXX
...X..X.X....X.X.X.X.X..XXXXXXX
.X..X....X.X.....XX....XXXXXXXX
..X..XX.X.X..XX.X..XX.XXXXXXXXX
.XXX.X.....X.X.X*.X.XX.XXXXXXXX
X..X..X.X.X.....X....X..XXXXXXX
..X.X....X..XXXX..XXX..XXXXXXXX
X....XXX..X.....X...X.XXXXXXXXX
..XX.....X.X.X.X..X.X..XXXXXXXX
XX.X.X.X...X.XX.X..X..X..XXXXXX
.M...XXXX.X.....X.X.X...XXXXXXX
X.XXX..X...X.X.X..X..X.XXXXXXXX
.XX...X.XX..X..X.X.X....XXXXXXX
....X......X..X......XXX.XXXXXX
X.X.XX.XXX..X.X.XX.XX.....XXXXX
X..X..X....XX.....X...X.X..XXXX
..X.X...XX....X.XX..X.X..XX.XXX
.X..X.X.X.X.XX...X.X.X.XX...XXX
XX.X...X....X..X........XX.X.XX
.....XX..X.X.XX..XX.X.X......XX
X.X.XX..X.XX....X..XXXXX.XXXX.X
XX..X.XX....XXX...X.X.X........
.XXXX...XXX.....X......XX.XX.XX
......XX....X.X..XX.XX...XX.XXX
X.X.X....X.X...X...X...X.....X.
XX...X.X..X..X.XXXX.XX.X.X.X...
XXXX..X..XXX.X......X.X...X..XX
XXX..XXX..X..XX.X.X....XX..X..X
X.XX..XX.X..X...X..X.X.XX.X..XX
...XXXX..X.X..X..X..XXX...XXXXX
XX...X..XX.XX..X..X.XX..X..XXXX
XX.XX..XXXXX.X.X.X...X.XXXXXXXX
X.....X.XXX..X.X..X.XXXXXXXXXXX
..X.X......X...X.X..XXXXXXXXXXX
20
3 41
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
M.......................................*
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
20
5 11
..........*
.XXXXXXXXXX
...........
XXXXXXXXXX.
M..........
0
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
4
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
40
5 17
XXXXXXXXXXXXXXXXX
XXX.XX.XXXXXXXXXX
XX.*..M.XXXXXXXXX
XXX.XX.XXXXXXXXXX
XXXXXXXXXXXXXXXXX
1
41 41
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
M........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.*.......................................
280
41 41
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
M........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.*.......................................
281
41 41
.X.XXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.
...XXXXXXXXXXXXXXXXXXX...................
.X..X.X.X.X.X.X.X..XXXX*X.X.X.X.X.X.X.XX.
.XXXX.X.X.X.X.X.X.XX.X.X.X.X.X.X.X.X.X.X.
.........................................
.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XX.X.X.X.XX.X.XX.X.X.X.X.X.X.X.X.X.X.X.X
.X.X.X.X.X.XXX.X.X.X.X.X.X.X.X.X.X.X.X.X.
X........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.X.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.XX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XMX.
.X....................................X..
..X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.X...................................X...
.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.XX.XXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
294
Oops!
Impressed
Impressed
Oops!
Oops!
Impressed
Impressed
Oops!
Impressed
+++++++++++++++++++++++++++++++++++++++++
9
37 31
X.XXXX.XX....X.XX...X.XXXXXXXXX
X.XXX...XXX.X..XXX.XX..XXXXXXXX
...X.XX..X...X..XX.X..XXXXXXXXX
X.X..X..X.X.X..X.....XX.XXXXXXX
...X..X.X....X.X.X.X.X..XXXXXXX
.X..X....X.X.....XX....XXXXXXXX
..X..XX.X.X..XX.X..XX.XXXXXXXXX
.XXX.X.....X.X.X*.X.XX.XXXXXXXX
X..X..X.X.X.....X....X..XXXXXXX
..X.X....X..XXXX..XXX..XXXXXXXX
X....XXX..X.....X...X.XXXXXXXXX
..XX.....X.X.X.X..X.X..XXXXXXXX
XX.X.X.X...X.XX.X..X..X..XXXXXX
.M...XXXX.X.....X.X.X...XXXXXXX
X.XXX..X...X.X.X..X..X.XXXXXXXX
.XX...X.XX..X..X.X.X....XXXXXXX
....X......X..X......XXX.XXXXXX
X.X.XX.XXX..X.X.XX.XX.....XXXXX
X..X..X....XX.....X...X.X..XXXX
..X.X...XX....X.XX..X.X..XX.XXX
.X..X.X.X.X.XX...X.X.X.XX...XXX
XX.X...X....X..X........XX.X.XX
.....XX..X.X.XX..XX.X.X......XX
X.X.XX..X.XX....X..XXXXX.XXXX.X
XX..X.XX....XXX...X.X.X........
.XXXX...XXX.....X......XX.XX.XX
......XX....X.X..XX.XX...XX.XXX
X.X.X....X.X...X...X...X.....X.
XX...X.X..X..X.XXXX.XX.X.X.X...
XXXX..X..XXX.X......X.X...X..XX
XXX..XXX..X..XX.X.X....XX..X..X
X.XX..XX.X..X...X..X.X.XX.X..XX
...XXXX..X.X..X..X..XXX...XXXXX
XX...X..XX.XX..X..X.XX..X..XXXX
XX.XX..XXXXX.X.X.X...X.XXXXXXXX
X.....X.XXX..X.X..X.XXXXXXXXXXX
..X.X......X...X.X..XXXXXXXXXXX
20
3 41
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
M.......................................*
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
29
5 11
..........*
.XXXXXXXXXX
...........
XXXXXXXXXX.
M..........
0
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
4
5 17
XXXXXXXXXXXXXXXXX
XXX.XX.XXXXXXXXXX
XX.*..M.XXXXXXXXX
XXX.XX.XXXXXXXXXX
XXXXXXXXXXXXXXXXX
1
41 41
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
M........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.*.......................................
280
41 41
.X.XXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.
...XXXXXXXXXXXXXXXXXXX...................
.X..X.X.X.X.X.X.X..XXXX*X.X.X.X.X.X.X.XX.
.XXXX.X.X.X.X.X.X.XX.X.X.X.X.X.X.X.X.X.X.
.........................................
.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.XX.X.X.X.XX.X.XX.X.X.X.X.X.X.X.X.X.X.X.X
.X.X.X.X.X.XXX.X.X.X.X.X.X.X.X.X.X.X.X.X.
X........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
.X.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.XX
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XMX.
.X....................................X..
..X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.X...................................X...
.XX.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.XX.XXXX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XX.
.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.
.........................................
294
5 11
..........*
.XXXXXXXXXX
...........
XXXXXXXXXX.
M..........
2
5 17
XXXXXXXXXXXXXXXXX
XXX.XX.XXXXXXXXXX
XX.*..M.XXXXXXXXX
XXX.XX.XXXXXXXXXX
XXXXXXXXXXXXXXXXX
1

Oops!
Oops!
Impressed
Oops!
Impressed
Impressed
Impressed
Oops!
Impressed
+++++++++++++++++++++++++++++++++++++++++++



"""
