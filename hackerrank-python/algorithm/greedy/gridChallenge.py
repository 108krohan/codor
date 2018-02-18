"""Grid challenge at hackerrank.com
"""
"""
Sample Input

1
5
ebacd
fghij
olmkn
trpqs
xywuv

Sample Output

YES

Explanation

The grid in the first and only testcase can be reordered to

abcde
fghij
klmno
pqrst
uvwxy

This fulfills the condition since the rows 1, 2, ..., 5 and the columns 1, 2, ..., 5 are all lexicographically sorted.
"""

def check(data, N) :

    for index in range(N) :
        for loop in range(N - 1) :
            if data[loop][index] > data[loop+1][index] :
                return False
    return True


cases = int(raw_input())

for _ in range(cases) :

    N = int(raw_input())
    data = [raw_input() for times in range(N)]

##    print data

    for index in range(N) :
        row = list(data[index])
        for loop in range(N - 1) :
            subindex = loop
            while subindex >= 0 and row[subindex] > row[subindex+1]:
                row[subindex+1], row[subindex] = row[subindex], row[subindex+1]
                subindex -= 1
        data[index] = ''.join(row)
    print data
    
    if check(data, N) :
        print 'YES'
    else :
        print "NO"
        
