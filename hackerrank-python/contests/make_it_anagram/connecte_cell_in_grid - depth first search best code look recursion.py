"""connected cell in a Grid at hackerrank.com"""

dire = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def dfs(i, j, mat, mark, color):
    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]): return
    if mat[i][j] == 0: return
    if mark[i][j] != -1: return
    mark[i][j] = color
    for d in dire:
        dfs(i+d[0], j + d[1], mat, mark, color)
        
N = int(raw_input())
M = int(raw_input())
mat = []
for i in xrange(N):
    mat.append(map(int, raw_input().split()))
mark = [ [-1]*M for i in xrange(N)]
c = 0
for i in xrange(N):
    for j in xrange(M):
        dfs(i, j, mat, mark, c)
        c += 1
print '\n'.join([str(elem) for elem in mark])
count = [0]*(N*M)
for i in xrange(N):
    for j in xrange(M):
        if mark[i][j] != -1:
            count[mark[i][j]] += 1
            
print max(count)
"""
https://www.hackerrank.com/contests/magic-lines-september-2015/challenges/connected-cell-in-a-grid-magic-lines
"""
"""
Sample Input:

4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0
Sample Output:

5
Task: 
Write the complete program to find the number of cells in the largest region.

Explanation

X X 0 0
0 X X 0
0 0 X 0
1 0 0 0
"""
