"""maximise sum at hackerrank.com
"""
"""
Problem statement

Get maximum of sum of subarray modulo M where M is given.
Subarray is a continuous subset of array elements.

Sample Input

1
5 7
3 3 9 9 5

Sample Output

6

Explanation

Max Possible Sum taking Modulo 7 is 6 , and we can get 6 by
adding first and second element of the array
"""

cases = int(raw_input())

for _ in range(cases) :

    size, modulo = map(int, raw_input().split())
    integers = map(int, raw_input().split())
    maxVal = 0
    for index in range(size) :
        found = False
        series_sum = 0
        for subindex in range(index, size) :
            series_sum += sum(integers[index:subindex + 1])%modulo
            
        


##    for index in range(size) :
##        rightSeriesSum = 0
##        leftSeriesSum = 0
##        found = 0
##        for subindex in range(index, size) :
##            rightSeriesSum += integers[subindex]
##            if rightSeriesSum % M > maxVal :
##                maxVal = rightSeriesSum
##            if maxVal == M - 1 :
##                found = 1
##                break
##        if found == 1 :
##            break

##        for subindex in range(index+1) :
##            leftSeriesSum += integers[subindex]
##            if leftSeriesSum % M > maxVal :
##                maxVal = rightSeriesSum
##            if maxVAl == M - 1 :
##                found = 1
##                break
##        if found == 1 :
##            break

##    print maxVal

    
    
