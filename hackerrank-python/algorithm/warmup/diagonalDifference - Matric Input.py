# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
rows = []
for i in range(N) :
    rows.append(raw_input().split()) ## rows[i] won't work, IndexError List index out of range
dsum = 0
isum = 0
for j in range(N) :
    dsum += int(rows[j][j])
    isum += int(rows[j][N-j-1])
print abs(dsum - isum)
